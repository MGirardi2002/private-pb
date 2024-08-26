import boto3
import csv

aws_access_key_id = "ASIAQEIP27PQYDFLUL3R"
aws_secret_access_key = "DaFZnp1AraoLebP1xszPberKLsvXJ/fbRDu9cHMd"
aws_session_token = "IQoJb3JpZ2luX2VjENz//////////wEaCXVzLWVhc3QtMSJIMEYCIQCikcqSht05/1Nj4hTeXS7afpJE5t5Tw009+3KCHg/cAwIhAIbhKt3H4tG3l7zt1Jre95SABa1IxYZG56sAhHGxD5LOKqwDCOX//////////wEQABoMMDA5MTYwMDMxMjAxIgw3BFjQEkpgFYv6Nz0qgAN6yWF7qnCrbayyfmgUOgV8a3jGkbbk5/JtP7CrzY9TSrJWaPUdY16yqeL/OAqmPchxwyPT+B426Tu9W8NZeN6WkHkAKyPz0wM4YPcx4JBXSS/Wb248SvrIZcs8YZ6QUUYZnc1NYeDecdgKno3nWuzccDAkKKtTibmpIvO1dGdIPl8O1nufcTygFf9dG/1ozqY/WRvhzW/XvXVNOhGa+ICh2gMtgUIuYRzN7qq2ZP3gOt9gMGXgWjYXix6z8TDnc6KPW7Wp+DWCEumSjmcQiDzAO/NYthQ89DWDdeLyl8ToalQMtJNLrpdqt2TjIzq/opzvpOn85WXZchM02RjmnAb04M6cLkAyijmv9yzusGcZ6PlcGWkhWuRgL6YIZmfdYrtt9fVLBcRIZn6hQvcRC4aM/Ctd5YxbYg2oMUj/YvnC1orinrf1Z8OuY0MkBZ4ZtZAAnnN6ptBlZyBwDXrqWmiJaYWb8D8DpNiMKJE8SumZPhmE5gKxvNXdy5nTKn3Bcx0w8PqvtgY6pQGrbFEv801J2c/Vl/xMO0bP2hkO44xAVz3b+B7DW6teNcGb5GK5yeq/uRu9/mejV8Ss5kqLksoRPr/wCnjZ3TwOV1twNgKh7gJcP7x7N4YwWiI2sQnse8Wg45QT5wLd4Hz8oTdGDr1pkiWJwjNwJqTFY+VW1bh5GBDRxndBO7bX8YcbVzgksFH80nBAWZnh3IdwDTJuETRXMWxbneVEhw62LqpNjDU="
region_name = "us-east-1"

bucket_name = "bucket-desafio"
file_key = "repasse-s-processado.csv"

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
    CAST(s."Total Repassado" AS DECIMAL) * 1.0 AS Total_Repassado_Convertido,
    CASE 
        WHEN s."Entidade" = 'SENAR' THEN 'Entidade SENAR'
        ELSE 'Entidade SENAI'
    END AS Tipo_Entidade,
    LOWER(s."Entidade") AS Entidade_Minuscula
FROM S3Object s
WHERE 
    s."Entidade" = 'SENAR'
    OR s."Entidade" = 'SENAI'
"""

try:
    results = s3_select_query(bucket_name, file_key, query)

    with open("resultados.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        for result in results:
            linha = result.strip().split(";")
            writer.writerow(linha)

    print("Consulta realizada com sucesso. Resultados salvos em 'resultados.csv'.")
except Exception as e:
    print(f"Ocorreu um erro ao executar a consulta: {e}")
