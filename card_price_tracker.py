import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_card_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        card_name = soup.find('h1', id='product_name').text.strip()
        prices = {}

        # Extract raw prices for various grades
        price_elements = soup.find_all('span', class_='price js-price')
        if len(price_elements) >= 6:
            prices['Raw'] = price_elements[0].text.strip()
            prices['PSA 7'] = price_elements[1].text.strip()
            prices['PSA 8'] = price_elements[2].text.strip()
            prices['PSA 9'] = price_elements[3].text.strip()
            prices['PSA 9.5'] = price_elements[4].text.strip()
            prices['PSA 10'] = price_elements[5].text.strip()

        return card_name, prices
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None, None
    except AttributeError:
        print("Card name or price not found on the page.")
        return None, None

if __name__ == "__main__":
    # Prompt for the text file
    file_path = input("Enter the path to the text file containing the URLs: ")

    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)

    all_card_data = []
    for url in urls:
        card_name, prices = get_card_data(url)
        if card_name and prices:
            card_data = {'Card Name': card_name, **prices}
            all_card_data.append(card_data)

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(all_card_data)
    df.to_excel('card_prices.xlsx', index=False)
    print("Card prices saved to card_prices.xlsx")