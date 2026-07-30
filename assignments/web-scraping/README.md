# 📘 Assignment: Web Scraping with Python

## 🎯 Objective

Learn how to extract data from websites using Python's `requests` and `BeautifulSoup` libraries, and save the scraped data to structured files for further analysis.

## 📝 Tasks

### 🛠️ Set Up Your Scraper

#### Description
Install the required libraries and build the core functions that will fetch web pages and parse their HTML content.

#### Requirements
Completed program should:

- Install `requests` and `beautifulsoup4` using `pip`
- Write a function `fetch_page(url)` that downloads a webpage's HTML and returns the response text
- Write a function `parse_html(html)` that creates a `BeautifulSoup` object for parsing
- Handle HTTP errors gracefully (e.g., catch connection errors, check for 404 status codes)
- Print a friendly error message and return `None` if the page cannot be fetched


### 🛠️ Extract Data from a Website

#### Description
Scrape structured data from a practice website — for example, quotes from `http://quotes.toscrape.com`. Extract meaningful fields from the HTML and store them in a Python list.

#### Requirements
Completed program should:

- Identify at least **three** different data fields to extract (e.g., quote text, author name, tags)
- Use BeautifulSoup methods such as `.find()`, `.find_all()`, and `.select()` to locate HTML elements
- Clean the extracted text by stripping leading/trailing whitespace
- Handle missing data gracefully (skip or mark incomplete entries)
- Store each item as a dictionary and collect all items into a list


### 🛠️ Save Scraped Data to Files

#### Description
Write the collected data to both CSV and JSON formats so it can be reused later for analysis or reporting.

#### Requirements
Completed program should:

- Save the scraped data to a **CSV file** (`scraped_data.csv`) with proper column headers
- Save the same data to a **JSON file** (`scraped_data.json`)
- Print a confirmation message showing how many items were saved to each file
- Verify that the saved files are readable and correctly formatted

## 📦 Starter Code

The `starter-code.py` file provides a basic scaffold with the `fetch_page()` and `parse_html()` functions already started for you.

## 📚 Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://docs.python-requests.org/)
- Practice site: [quotes.toscrape.com](http://quotes.toscrape.com)
