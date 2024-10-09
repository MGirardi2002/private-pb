import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col
from datetime import datetime

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

json_path = "s3://meubuckets6/Raw/TMDB/JSON/2024/10/08/"

dynamic_frame_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path], "recurse": True},
    format="json",
    format_options={"jsonPath": "$", "schemaEvolution": True},
)

dataframe_json = dynamic_frame_json.toDF()
dataframe_json = dataframe_json.filter(col("imdb_id").isNotNull())
dataframe_json = dataframe_json.dropDuplicates(["imdb_id"])
dataframe_json = dataframe_json.repartition(1)

current_date = datetime.now()
ano_atual = current_date.strftime("%Y")
mes_atual = current_date.strftime("%m")
dia_atual = current_date.strftime("%d")

output_path_s3 = (
    f"s3://meubuckets6/Trusted/dados_parquet/{ano_atual}/{mes_atual}/{dia_atual}/"
)

dataframe_json.write.mode("append").parquet(output_path_s3)
job.commit()
