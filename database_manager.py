import sqlite3
import pandas as pd

def create_table():
    conn = sqlite3.connect('crypto_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cryptocurrencies
                 (Name TEXT, Symbol TEXT, MarketCap REAL, Price REAL, Volume REAL)''')
    conn.commit()
    conn.close()

def insert_data(df):
    conn = sqlite3.connect('crypto_data.db')
    df.to_sql('cryptocurrencies', conn, if_exists='replace', index=False)
    conn.close()

def fetch_data():
    conn = sqlite3.connect('crypto_data.db')
    df = pd.read_sql_query("SELECT * FROM cryptocurrencies", conn)
    conn.close()
    return df

def main():
    create_table()
    df = pd.read_csv("cryptocurrency_data.csv")
    insert_data(df)
    fetched_df = fetch_data()
    print(fetched_df.head())

if __name__ == "__main__":
    main()
