# Retail Sales Data Pipeline

This project demonstrates a complete data engineering pipeline for processing retail sales data.

## Project Structure
- **data_ingestion**: Scripts for ingesting data using Kafka.
- **data_processing**: ETL pipeline using PySpark.
- **data_storage**: SQL scripts and Python code to load data into a PostgreSQL database.
- **data_visualization**: Jupyter notebook for generating reports.
- **orchestration**: Airflow DAG to schedule and manage the pipeline.

## How to Run
1. Start Kafka and produce data using `kafka_producer.py`.
2. Run the ETL pipeline using `etl_pipeline.py`.
3. Load data into the database using `load_data.py`.
4. Generate reports using `report.ipynb`.
5. Use the Airflow DAG to orchestrate the pipeline.

## Requirements
- Apache Kafka
- Apache Spark
- PostgreSQL
- Python 3.x
- Airflow (Optional)
- Docker (Optional)

## Author
Sethu Prakash
