import sys
from datetime import datetime
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import trim, col, lit

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

csv_path = "s3://meubuckets6/Raw/Local/CSV/Movies/2024/09/09/"

csv_df = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", "|")
    .option("inferSchema", "true")
    .load(csv_path + "movies.csv")
)

movies_columns = csv_df.columns

for column in movies_columns:
    csv_df = csv_df.withColumn(column, trim(col(column)))

csv_df_filtered = (
    csv_df.filter(col("genero").contains("Sci-Fi"))
    .select("id", "tituloOriginal", "genero", "anoLancamento")
    .dropDuplicates(["id"])
)


current_date = datetime.now()
ano_atual = current_date.strftime("%Y")
mes_atual = current_date.strftime("%m")
dia_atual = current_date.strftime("%d")

output_path = (
    f"s3://meubuckets6/Trusted/dados_parquet/{ano_atual}/{mes_atual}/{dia_atual}/"
)

csv_df_filtered.coalesce(1).write.mode("append").parquet(output_path)

job.commit()
