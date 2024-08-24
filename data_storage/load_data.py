import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname='retaildb' user='username' host='localhost' password='password'")
cur = conn.cursor()

def load_data():
    df = pd.read_parquet('data/final_sales_data.parquet')
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO retail_sales (order_id, product_id, quantity, price, order_date) VALUES (%s, %s, %s, %s, %s)",
            (row['order_id'], row['product_id'], row['quantity'], row['price'], row['date'])
        )
    conn.commit()

if __name__ == "__main__":
    load_data()
