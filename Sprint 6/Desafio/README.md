# Desafio

O desafio em questão, pode ser basicamente definido apenas como a ingestão via batch dos dados que vão ser utilizados para o desafio final dentro de um Bucket S3 em RAW Zone. Para isso, foi usado um código Python para conectar à AWS com a lib boto3, ainda que executando dentro de um container Docker.


# Etapas

Primeiro, a definição do código python para iniciar a sessão na AWS, usando as credenciais do administrador (vazias no código).
[Arquivo connection.py](etapa-1/sprint_6/connection.py)

```
import boto3
from botocore.exceptions import NoCredentialsError

aws_access_key_id = ""
aws_secret_access_key = ""
aws_session_token = ""
region_name = ""

bucket_name = "meubuckets6"
CSV_PATH_MOVIES = "/app/data/movies.csv"
CSV_PATH_SERIES = "/app/data/series.csv"

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region_name,
)
s3 = session.client("s3")


def upload_to_s3(file_name, bucket, s3_file_name):
    try:
        s3.upload_file(file_name, bucket, s3_file_name)
        print(f"Upload bem-sucedido: {s3_file_name}")
    except FileNotFoundError:
        print(f"O arquivo {file_name} não foi encontrado.")
    except NoCredentialsError:
        print("Credenciais de AWS não encontradas.")
    except Exception as e:
        print(f"Erro ao fazer upload para o S3: {e}")


def main():

    s3_movies_path = "Raw/Local/CSV/Movies/2024/09/09/movies.csv"
    s3_series_path = "Raw/Local/CSV/Series/2024/09/09/series.csv"

    upload_to_s3(CSV_PATH_MOVIES, bucket_name, s3_movies_path)
    upload_to_s3(CSV_PATH_SERIES, bucket_name, s3_series_path)


if __name__ == "__main__":
    main()

```
O código, além de fazer a conexão, usa duas funções, a upload_to_s3, que serve para upar arquivos dentro do S3, e a main, que define os caminhos dos arquivos CSV e chama a função de upload para enviá-los para o bucket.

Em seguida, é usado o Dockerfile para criar a imagem com o comando "build", e assim que o comando "run", o arquivo python é acionado e realiza o upload dos arquivos dentro do bucket.

[Dockerfile](etapa-1/sprint_6/Dockerfile)
```
FROM python:3.9

RUN pip install boto3

WORKDIR /app

COPY connection.py .

VOLUME /app/data

CMD ["python", "connection.py"]
```
***

## Questão do Desafio

O principal objetivo deste desafio é analisar a franquia Alien, focando no gênero de ficção científica. A ideia é investigar se, após o lançamento do primeiro filme da franquia, os filmes de ficção científica começaram a abordar com mais frequência o tema de extraterrestres. Para realizar essa análise, será utilizado o arquivo "movies.csv" e a API do TMDB. O plano é examinar as sinopses dos filmes da categoria de ficção científica, buscando por palavras-chave como "alien" e "aliens".

Com os dados obtidos, será criado um gráfico de barras dividido por décadas, para verificar se o filme Alien contribuiu para popularizar o tema de vida fora da Terra no cinema.




