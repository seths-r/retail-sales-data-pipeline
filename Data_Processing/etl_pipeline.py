from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('RetailSalesETL').getOrCreate()

def transform_data(input_df):
    transformed_df = input_df.withColumnRenamed('order_date', 'date')
    return transformed_df

def main():
    input_df = spark.read.json('data/raw_sales_data.json')
    transformed_df = transform_data(input_df)
    transformed_df.write.parquet('data/processed_sales_data.parquet')

if __name__ == "__main__":
    main()
