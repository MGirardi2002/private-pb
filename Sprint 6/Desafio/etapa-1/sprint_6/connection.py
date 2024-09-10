import boto3
from botocore.exceptions import NoCredentialsError

aws_access_key_id = "ASIAQEIP27PQ4HTAHDTX"
aws_secret_access_key = "1+EIY32CIYb5eh7fH7eWnY1lC2XTEBl9Mvy/rv2+"
aws_session_token = "IQoJb3JpZ2luX2VjEDcaCXVzLWVhc3QtMSJGMEQCIA7nYeqF/YeAot8epEVXuxweOoVArgqZuMgqW0qkW3k5AiA/2NyOC4VjkhvudsrJG1iZ90ZmRsxUjC6HzLq3+jcldyqjAwhfEAAaDDAwOTE2MDAzMTIwMSIMHqk2B5w9mV5zZ3fMKoADWSI/b/L+ESH6y6CRkPvgfl46Qv4VBHb/JF2GKUtwXtR5e6G3ONgkRnsbzaKVMHUQ57JNHXUXQwg5YYEr0DL1uEjqShSHuKfxWvfZKs1oWETJLUsXJ/ceQ0oyTUF/3VfICzYBgvjvjXXkX8BcaZFWlvfJy7oKBErYizbDMsuaIFbfHzLvcHIKN245a76iD9M7lb6tWMLvzmxLnPVmKTms2Bo111a3/h5nnaYtfkt5twjssvdANwQ1PZ64ctZpxRj+VEuoWGnisfizjLYA0qkk0k3bVapN/HxEok9k6zp9arIEVk06t4/hx5WwM+9Xo0rSatpKSL46YGpRKX6vuBW3H2xPIai++6Od2L7mXk97SnSc1PRYaVuGr2193svXfv4ZbQFgi/tqRdg3Eo3eiFHvdcJxZFgm3NkY+pTectrQ0OcsRt4Gx3BvuJnoMKWtT0aakTdte5tAoaztFufss3bqknMgq+YsfPaA0ELGamWB0oBYewxucf0/wPGUMBCw2fXeMJCD/LYGOqcBY1DJlW2Dff1J3fFaQPNJtzcxa/+r71in+x2O7pGRcnXL6XIOXyGLQ2pBAl8F9Y4ndz7onT2mYLs5Jwk6y1KZNnbbGL6OnWQwMjpskhp/E5Sjh2Q+RwtYF2W89Hxr6wKHB/EnDe14Z03/Nu7A6mY9fA2j277+3nCW60xX7YmjOnVY8zJDuc606PSVtYnOVP9K2z7yKbkHVkTo/CU5tiZbq+SeTU94hvU="
region_name = "us-east-1"

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
