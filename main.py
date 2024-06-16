import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def parse_crypto_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='cmc-table')
    rows = table.find_all('tr')[1:]
    data = []

    for row in rows:
        cols = row.find_all('td')
        name = cols[2].find('p').text
        symbol = cols[2].find('p', class_='coin-item-symbol').text
        market_cap = cols[3].text
        price = cols[4].text
        volume_24h = cols[6].text
        circulating_supply = cols[5].text

        data.append({
            'Name': name,
            'Symbol': symbol,
            'Market Cap': market_cap,
            'Price': price,
            'Volume (24h)': volume_24h,
            'Circulating Supply': circulating_supply
        })

    return data

def save_to_csv(data, filename='cryptocurrencies.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def visualize_data(data):
    df = pd.DataFrame(data)
    df['Market Cap'] = df['Market Cap'].str.replace('$', '').str.replace(',', '').astype(float)
    top_10 = df.nlargest(10, 'Market Cap')

    plt.figure(figsize=(14, 7))
    plt.bar(top_10['Name'], top_10['Market Cap'], color='teal')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Market Cap (USD)')
    plt.title('Top 10 Cryptocurrencies by Market Cap')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    url = 'https://coinmarketcap.com/'
    html = fetch_html(url)
    if html:
        data = parse_crypto_data(html)
        save_to_csv(data)
        visualize_data(data)
        print('Data successfully scraped, saved to CSV, and visualized.')
    else:
        print('Failed to retrieve the webpage.')

if __name__ == "__main__":
    main()
