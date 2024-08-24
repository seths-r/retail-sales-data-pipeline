from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('TransformationJob').getOrCreate()

def run_transformation():
    df = spark.read.parquet('data/processed_sales_data.parquet')
    df = df.filter(df.quantity > 0)
    df.write.parquet('data/final_sales_data.parquet')

if __name__ == "__main__":
    run_transformation()
