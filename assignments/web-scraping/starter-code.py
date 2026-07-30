# Starter Code: Web Scraping with Python

import requests
from bs4 import BeautifulSoup
import csv
import json


def fetch_page(url):
    """Fetch a webpage and return its HTML content."""
    # TODO: Send a GET request to the URL
    # TODO: Check if the request was successful (status code 200)
    # TODO: Return the response text
    # TODO: Handle exceptions (connection errors, timeouts, etc.)
    pass


def parse_html(html):
    """Parse HTML string into a BeautifulSoup object."""
    # TODO: Create a BeautifulSoup object using 'html.parser'
    pass


def extract_quotes(soup):
    """Extract quotes, authors, and tags from the parsed HTML."""
    quotes = []
    # TODO: Find all quote containers on the page
    # TODO: For each container, extract:
    #   - The quote text
    #   - The author name
    #   - The list of tags
    # TODO: Append each quote as a dictionary to the quotes list
    # TODO: Handle cases where data might be missing
    return quotes


def save_to_csv(quotes, filename="scraped_data.csv"):
    """Save the list of quote dictionaries to a CSV file."""
    # TODO: Open a CSV file for writing
    # TODO: Write a header row with field names
    # TODO: Write each quote as a row in the CSV
    pass


def save_to_json(quotes, filename="scraped_data.json"):
    """Save the list of quote dictionaries to a JSON file."""
    # TODO: Open a JSON file for writing
    # TODO: Write the quotes list to the file with proper indentation
    pass


def main():
    url = "http://quotes.toscrape.com"
    print(f"Fetching page: {url}")

    html = fetch_page(url)
    if html is None:
        print("Failed to fetch the page. Exiting.")
        return

    soup = parse_html(html)
    quotes = extract_quotes(soup)
    print(f"Extracted {len(quotes)} quotes.")

    save_to_csv(quotes)
    save_to_json(quotes)
    print("Done! Data saved to scraped_data.csv and scraped_data.json.")


if __name__ == "__main__":
    main()
