import crypto_scraper
import data_analyzer
import api_handler
import visualizer
import database_manager

def run_crypto_analysis():
    print("Scraping data from CoinMarketCap...")
    df = crypto_scraper.main()

    print("\nAnalyzing data...")
    data_analyzer.main()

    print("\nFetching real-time data from API...")
    api_handler.main()

    print("\nCreating visualizations...")
    visualizer.main()

    print("\nStoring data in database...")
    database_manager.main()

    print("\nCrypto analysis complete!")

if __name__ == "__main__":
    run_crypto_analysis()
