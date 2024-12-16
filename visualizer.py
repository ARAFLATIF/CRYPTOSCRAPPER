import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_market_cap_chart(df):
    top_10 = df.nlargest(10, "Market Cap")
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Symbol", y="Market Cap", data=top_10)
    plt.title("Top 10 Cryptocurrencies by Market Cap")
    plt.xlabel("Cryptocurrency Symbol")
    plt.ylabel("Market Cap (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top_10_cryptocurrencies.png")
    plt.close()

def create_market_dominance_pie(df):
    top_5 = df.nlargest(5, "Market Dominance")
    others = pd.Series({"Name": "Others", "Market Dominance": 100 - top_5["Market Dominance"].sum()})
    data = top_5.append(others, ignore_index=True)

    plt.figure(figsize=(10, 8))
    plt.pie(data["Market Dominance"], labels=data["Name"], autopct='%1.1f%%', startangle=90)
    plt.title("Cryptocurrency Market Dominance")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig("market_dominance_pie.png")
    plt.close()

def main():
    df = pd.read_csv("cryptocurrency_data.csv")
    create_market_cap_chart(df)
    create_market_dominance_pie(df)
    print("Charts have been created and saved.")

if __name__ == "__main__":
    main()
