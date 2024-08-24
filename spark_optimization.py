from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import IntegerType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("OptimizedSparkJob") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.sql.autoBroadcastJoinThreshold", "10485760") \
    .getOrCreate()

# Set up logging level to WARN to avoid verbose logs
spark.sparkContext.setLogLevel("WARN")

# Load data from a CSV file
df = spark.read.option("header", "true").csv("path/to/input.csv")

# Cache the dataframe if it will be used multiple times
df.cache()

# Example of data transformation with optimizations
df_transformed = df \
    .filter(col("column1").isNotNull()) \
    .withColumn("new_column", col("existing_column") * lit(2)) \
    .groupBy("group_column") \
    .agg({"numeric_column": "sum"}) \
    .withColumnRenamed("sum(numeric_column)", "total")

# Broadcast a small dataframe for optimization
small_df = spark.read.option("header", "true").csv("path/to/small.csv")
broadcasted_small_df = spark.sparkContext.broadcast(small_df.collect())

# Join operation with a broadcasted dataframe
df_joined = df_transformed.join(
    spark.createDataFrame(broadcasted_small_df),
    on="join_column",
    how="inner"
)

# Perform an action to trigger the computation
df_joined.show()

# Unpersist the dataframe after its use to free up memory
df.unpersist()

# Save the result to an output path
df_joined.write.mode("overwrite").parquet("path/to/output.parquet")

# Stop the Spark session
spark.stop()
