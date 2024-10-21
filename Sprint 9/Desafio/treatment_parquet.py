import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

parquet_path = "pathing"

df = spark.read.parquet(parquet_path)
df_filtered = df.filter(
    df["id"].isNotNull()
    & df["overview"].isNotNull()
    & (df["overview"] != "")
    & df["release_date"].isNotNull()
    & (df["release_date"] != "")
    & (col("release_date").rlike("^\d{4}-\d{2}-\d{2}$"))
)

output_path = f"s3://meubuckets6/Trusted/dados_tratados_prontos/"
df_filtered.write.mode("append").parquet(output_path)

job.commit()
