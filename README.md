Card Price Tracker

This Python script scrapes card prices from specified URLs and saves the data to an Excel file.

Prerequisites

Python 3.6 or higher
Required packages: requests, beautifulsoup4, pandas, openpyxl (for saving to Excel)

Installation

Install the necessary packages using pip:
Bash

pip install requests beautifulsoup4 pandas openpyxl

Usage

Create a text file: List each card URL on a separate line in a text file (e.g., card_urls.txt).
Run the script: Execute the script from your terminal: python card_price_tracker.py
Enter file path: When prompted, provide the path to your text file (e.g., card_urls.txt). Exclude the quotes when inputting the path.
Output: The script will generate an Excel file named card_prices.xlsx containing the card names and prices.
Example Text File (card_urls.txt)

https://www.example-card-website.com/card1
https://www.example-card-website.com/card2
https://www.example-card-website.com/card3
Notes

The script currently extracts the Raw, PSA 7, PSA 8, PSA 9, PSA 9.5, and PSA 10 prices.
Ensure that the URLs point to valid pages with the expected HTML structure.
Error handling is included to catch invalid URLs and missing data.

Disclaimer

This script is intended for personal use and educational purposes. Always respect the terms of service of the websites you are scraping.
