import os
import zipfile
import subprocess
import boto3

aws_access_key_id = ""
aws_secret_access_key = ""
aws_session_token = ""

lambda_function_name = "tmdb-data-injection"
role_arn = ""
layer_arn = ""
tmdb_api_key = ""
s3_bucket = "meubuckets6"

codigo_lambda = """
import json
import os
from datetime import datetime
import requests
import boto3

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

SCI_FI_GENRE_ID = 878
FANTASY_GENRE_ID = 14

def buscar_detalhes_filme(filme_id):
    url = f"https://api.themoviedb.org/3/movie/{filme_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Erro ao buscar detalhes do filme {filme_id}: {response.status_code}")
        return {}

    detalhes = response.json()
    return detalhes

def buscar_filmes(page=1):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'with_genres': f'{SCI_FI_GENRE_ID},{FANTASY_GENRE_ID}',
        'page': page
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Erro na requisição: {response.status_code}")
        return []

    data = response.json()
    results = data.get('results', [])
    
    filmes = []
    for movie in results:
        # Pegar detalhes adicionais (budget) de cada filme
        detalhes = buscar_detalhes_filme(movie['id'])

        filme = {
            'id': movie['id'],
            'title': movie['title'],
            'budget': detalhes.get('budget', 0),
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
            'overview': movie.get('overview', 'N/A')
        }
        filmes.append(filme)
    
    return filmes, data.get('total_pages', 1)

def salvar_dados_s3(dados, nome_lote):
    s3 = boto3.client('s3')
    data_atual = datetime.now()
    ano = data_atual.strftime('%Y')
    mes = data_atual.strftime('%m')
    dia = data_atual.strftime('%d')

    for i in range(0, len(dados), 100):
        lote = dados[i:i + 100]
        nome_arquivo = f'{nome_lote}_{i // 100 + 1}.json'
        caminho_s3 = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/{nome_arquivo}"

        caminho_temp = f"/tmp/{nome_arquivo}"
        with open(caminho_temp, 'w', encoding='utf-8') as f:
            json.dump(lote, f, ensure_ascii=False, indent=4)
        
        print(f'Salvando {len(lote)} registros no arquivo {nome_arquivo}')

        try:
            s3.upload_file(caminho_temp, S3_BUCKET_NAME, caminho_s3)
            print(f"Arquivo {nome_arquivo} carregado com sucesso para {caminho_s3}")
        except Exception as e:
            print(f"Erro ao carregar o arquivo no S3: {e}")

def lambda_handler(event, context):
    todos_filmes = []
    pagina = 1
    total_paginas = 1
    max_filmes = 100

    print('Buscando filmes Sci-Fi e Fantasy...')

    while pagina <= total_paginas and len(todos_filmes) < max_filmes:
        filmes, total_paginas = buscar_filmes(pagina)
        
        restantes = max_filmes - len(todos_filmes)
        todos_filmes.extend(filmes[:restantes])

        print(f"Página {pagina} de {total_paginas} processada com {len(filmes)} filmes.")
        
        if pagina >= 500 or len(todos_filmes) >= max_filmes:
            print("Limite de páginas ou de filmes atingido. Parando busca.")
            break
        pagina += 1

    salvar_dados_s3(todos_filmes, 'Filmes_SciFi_Fantasy')

    return {
        'statusCode': 200,
        'body': json.dumps('Filmes de Sci-Fi e Fantasy carregados no S3.')
    }
"""


def criar_pacote(diretorio_pacote):
    subprocess.check_call([os.sys.executable, "-m", "venv", "env"])
    subprocess.check_call(
        [
            os.path.join("env", "Scripts", "pip"),
            "install",
            "requests",
            "-t",
            diretorio_pacote,
        ]
    )


def criar_zip(caminho_zip, diretorio_pacote, nome_arquivo, conteudo):
    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(diretorio_pacote):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, diretorio_pacote))

        zipf.writestr(nome_arquivo, conteudo)


def criar_atualizar_lambda():
    sessao = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name="us-east-1",
    )

    client = sessao.client("lambda")

    diretorio_pacote = "pacote"
    caminho_zip = "lambda_funcao.zip"

    if os.path.exists(diretorio_pacote):
        for root, dirs, files in os.walk(diretorio_pacote, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(diretorio_pacote)

    os.makedirs(diretorio_pacote)

    criar_pacote(diretorio_pacote)

    criar_zip(caminho_zip, diretorio_pacote, "lambda_function.py", codigo_lambda)

    try:
        client.get_function(FunctionName=lambda_function_name)
        funcao_existe = True
    except client.exceptions.ResourceNotFoundException:
        funcao_existe = False

    if funcao_existe:
        print(f"Atualizando a função Lambda {lambda_function_name}...")
        response = client.update_function_code(
            FunctionName=lambda_function_name, ZipFile=open(caminho_zip, "rb").read()
        )
        print(f"Função Lambda {lambda_function_name} atualizada com sucesso.")
    else:
        print(f"Criando a função Lambda {lambda_function_name}...")
        response = client.create_function(
            FunctionName=lambda_function_name,
            Runtime="python3.9",
            Role=role_arn,
            Handler="lambda_function.lambda_handler",
            Code={"ZipFile": open(caminho_zip, "rb").read()},
            Description="Função Lambda para buscar dados do TMDB e salvar no S3",
            Timeout=300,
            MemorySize=128,
            Environment={
                "Variables": {"TMDB_API_KEY": tmdb_api_key, "S3_BUCKET_NAME": s3_bucket}
            },
            Layers=[layer_arn],
        )
        print(f"Função Lambda {lambda_function_name} criada com sucesso.")


if __name__ == "__main__":
    criar_atualizar_lambda()
