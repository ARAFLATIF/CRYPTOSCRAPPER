import requests
from config import API_KEY, API_URL

def fetch_crypto_data(symbol):
    params = {
        'symbol': symbol,
        'convert': 'USD'
    }
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY
    }
    response = requests.get(API_URL, params=params, headers=headers)
    data = response.json()
    return data['data'][symbol]

def main():
    btc_data = fetch_crypto_data('BTC')
    print(f"Bitcoin Price: ${btc_data['quote']['USD']['price']:.2f}")
    print(f"24h Change: {btc_data['quote']['USD']['percent_change_24h']:.2f}%")

if __name__ == "__main__":
    main()
