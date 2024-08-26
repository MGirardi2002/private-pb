import boto3
import csv

aws_access_key_id = "ASIAQEIP27PQ24IPEFKM"
aws_secret_access_key = "pQKkWVmUiOGL5YyH/g0VInXdpHyYOF+kKMLzxKp4"
aws_session_token = "IQoJb3JpZ2luX2VjENP//////////wEaCXVzLWVhc3QtMSJGMEQCIAE6T385mEGBarPz3WJpVE98BRCbxD6jNgYsKjGZw6BfAiApX1QhGnyjUv0DoJ7DEUoUTiuvKtO4kmCQ/SJKfry/tCqsAwjb//////////8BEAAaDDAwOTE2MDAzMTIwMSIMwpZ+L5mUNdrPHYWUKoADPGA2ODml0P4bsuayD5ebJZbm26ueqvt69bdCC6UvJUffclf/WE/b+vecVA8C4KQjBnd8nukWFyhixucBwG91k2LK5qvsnjS+ZSnSA+QPEbLnO1JSxBFx6QLPKLk+hrfsMM6mRMMJ/npsyPXQMVVh0/EP8eTNQbsES+uTa/lJiH4IY4ugBAvPStGDYUsKuZOoyHhxX0BDLOOilk/FHq2QpoyrK+61i0/SB2nrXBabr3d8T5gfhjDCj5pp8T0HJz1i7MQMTvatoQ3tiJCKidgCDskjiX95wX9gGaniFKH/X6RLpukVJprccWYUGJHaAW+/uPij40dIMBp3jzQmr/ZSF1BRwNLYjnWsnnTA9arlKYVOdgLfgqDIttnS64xsA7XUQG7GBtmLZEBP3gCnfPAk4UtciIkPDtNfftzc/Z8lOPvIlnqn/7ISohdaYjQ3x7urfDEYa5hjtkTmbsdh1/bspcE6LlZpx/KF/jVXIWg614GFmkIu2lWN3E6PAvpBfaDtMI/qrbYGOqcBzFkiwtMHNF7TSBckaWmYhRYjsphJf7a3VZWGc+jPEUeDPcEB2f2guPzwPavUhQqWd2rX/McqtocfYDdFtmkBpIk1iIUZUinVHuCfFk/bk+R1oPVD2HPOar/8f9PnUi9QE4xaHMH3B+W1PzhEHAKlEhJ7plnjpIxPnfT5xEtmCIRzHXErj4Svf++dPRPRjJRA12RtQv66RBcZ10x/XtShCQ6OvPuBC4s="
region_name = "us-east-1"

bucket_name = "bucket-desafio"
file_key = "repasse-s.csv"

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region_name,
)
s3 = session.client("s3")


def s3_select_query(bucket, key, query, delimiter=";", has_header=True):
    file_header_info = "Use" if has_header else "None"
    response = s3.select_object_content(
        Bucket=bucket,
        Key=key,
        ExpressionType="SQL",
        Expression=query,
        InputSerialization={
            "CSV": {
                "FileHeaderInfo": file_header_info,
                "FieldDelimiter": delimiter,
            }
        },
        OutputSerialization={"CSV": {}},
    )

    records = []
    for event in response["Payload"]:
        if "Records" in event:
            records.append(event["Records"]["Payload"].decode("utf-8"))

    return records


query = """
    SELECT 
    s."Mês / Ano de Referência" AS Mes_Ano,
    s."Entidade",
    s."UC/CNPJ",
    s."Total Repassado",
    CASE 
        WHEN s."Entidade" = 'SENAR' THEN 'Entidade SENAR'
        ELSE 'Outras Entidades'
    END AS Tipo_Entidade,
    UPPER(s."Entidade") AS Entidade_Maiuscula
FROM S3Object s
WHERE 
    s."Entidade" IN ('SENAR', 'SENAI')
    AND s."Mês / Ano de Referência" LIKE 'jan/%'

"""

try:
    results = s3_select_query(bucket_name, file_key, query)

    with open("resultados.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        for result in results:
            writer.writerow(result.split(";"))

    print("Consulta realizada com sucesso. Resultados salvos em 'resultados.csv'.")
except Exception as e:
    print(f"Ocorreu um erro ao executar a consulta: {e}")
