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
