import pandas as pd
import numpy as np

def calculate_market_dominance(df):
    df['Market Cap'] = df['Market Cap'].str.replace('$', '').str.replace(',', '').astype(float)
    total_market_cap = df['Market Cap'].sum()
    df['Market Dominance'] = (df['Market Cap'] / total_market_cap) * 100
    return df

def calculate_price_change(df, days=7):
    # This is a placeholder. In a real scenario, you'd need historical data.
    df['Price Change (%)'] = np.random.uniform(-10, 10, df.shape[0])
    return df

def identify_top_gainers_losers(df):
    df_sorted = df.sort_values('Price Change (%)', ascending=False)
    top_gainers = df_sorted.head(5)
    top_losers = df_sorted.tail(5)
    return top_gainers, top_losers

def main():
    df = pd.read_csv("cryptocurrency_data.csv")
    df = calculate_market_dominance(df)
    df = calculate_price_change(df)
    top_gainers, top_losers = identify_top_gainers_losers(df)
    
    print("Top 5 Gainers:")
    print(top_gainers[['Name', 'Symbol', 'Price Change (%)']])
    print("\nTop 5 Losers:")
    print(top_losers[['Name', 'Symbol', 'Price Change (%)']])

if __name__ == "__main__":
    main()
