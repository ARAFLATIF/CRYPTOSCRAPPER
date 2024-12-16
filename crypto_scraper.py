import requests
from bs4 import BeautifulSoup
import pandas as pd
from config import COINMARKETCAP_URL

def scrape_coinmarketcap():
    response = requests.get(COINMARKETCAP_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    
    crypto_data = []
    rows = soup.select("tbody tr")
    
    for row in rows[:100]:
        name = row.select_one(".cmc-link")["title"]
        symbol = row.select_one(".coin-item-symbol").text
        market_cap = row.select_one(".sc-edc9a476-1.gqomIJ")["title"]
        price = row.select_one(".sc-cadad039-0.clgqXO")["title"]
        volume = row.select_one(".sc-edc9a476-1.dBJPYV")["title"]
        
        crypto_data.append({
            "Name": name,
            "Symbol": symbol,
            "Market Cap": market_cap,
            "Price": price,
            "Volume (24h)": volume
        })
    
    return pd.DataFrame(crypto_data)

def main():
    df = scrape_coinmarketcap()
    df.to_csv("cryptocurrency_data.csv", index=False)
    print("Data has been scraped and saved to cryptocurrency_data.csv")
    return df

if __name__ == "__main__":
    main()
