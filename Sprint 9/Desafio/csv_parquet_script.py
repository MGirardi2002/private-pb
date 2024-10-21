import sys
import requests
from datetime import datetime
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col


def get_tmdb_id(imdb_id, api_key):
    url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={api_key}&external_source=imdb_id"
    response = requests.get(url)
    data = response.json()
    if data["movie_results"]:
        return data["movie_results"][0]["id"]
    return None


def get_movie_details(tmdb_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    overview = data.get("overview", None)
    budget = data.get("budget", 0)
    popularity = data.get("popularity", 0)
    release_date = data.get("release_date", None)
    return overview, budget, popularity, release_date


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

parquet_path = "s3://meubuckets6/Trusted/dados_parquet/2024/10/09/"
df = spark.read.parquet(parquet_path)
api_key = "c91509146d3dbe59478fc432bb0de8fa"
df = (
    df.withColumnRenamed("id", "id_imdb")
    .withColumnRenamed("tituloOriginal", "title")
    .withColumnRenamed("anoLancamento", "release_date")
)


def fetch_tmdb_data(row):
    tmdb_id = get_tmdb_id(row["id_imdb"], api_key)
    overview, budget, popularity, release_date = (
        get_movie_details(tmdb_id, api_key)
        if tmdb_id
        else (None, 0, 0, row["release_date"])
    )
    return (
        tmdb_id,
        row["id_imdb"],
        row["title"],
        budget,
        release_date,
        popularity,
        overview,
    )


rdd = df.rdd.map(fetch_tmdb_data)
new_df = spark.createDataFrame(
    rdd,
    schema=[
        "id",
        "imdb_id",
        "title",
        "budget",
        "release_date",
        "popularity",
        "overview",
    ],
)

current_date = datetime.now()
ano_atual, mes_atual, dia_atual = (
    current_date.strftime("%Y"),
    current_date.strftime("%m"),
    current_date.strftime("%d"),
)
output_path = f"s3://meubuckets6/Trusted/parquet_csv_overview/{ano_atual}/{mes_atual}/{dia_atual}/"

new_df.write.mode("append").parquet(output_path)
job.commit()
