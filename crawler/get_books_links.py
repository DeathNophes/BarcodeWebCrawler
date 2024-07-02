# Getting the books links

# Importing necessary modules
from bs4 import BeautifulSoup
from helpers import books_links_csv_path, is_page_url_valid
import pandas as pd
import requests
import time
import os

# We read the file with links to the pages and use indexes to access certain range of them
current_pages = pd.read_csv(pages_links_books_csv_path)
pages_links = list(current_pages['Links'])[0:0]

# We create a dictionary to store books urls
books_urls = {'urls': []}

# We check if the path to the book links exists
if os.path.exists(books_links_csv_path):
    current_books_links = pd.read_csv(books_links_csv_path)
    books_links = set(current_books_links['urls'])
else:
    books_links = set()


def is_book_link_valid(book_link):
    if book_link in books_links:
        return False
    return True


def get_book_links():
    for url in pages_links:
        if not is_page_url_valid(url):
            continue

        html_text = requests.get(url).text

        soup = BeautifulSoup(html_text, 'lxml')
        books = soup.find_all('div', class_='col-xs-3 five-on-a-row')

        for book in books:

            products = book.find_all('a', class_='product-box')

            for product in products:
                href = product.get('href')
                if is_book_link_valid(href) and href not in books_urls['urls']:
                    books_urls['urls'].append(href)

        time.sleep(1)


def export_to_file_books_links(data):
    # Create a DataFrame
    df_book_links = pd.DataFrame.from_dict(data, orient='columns')

    # Check if the file exists
    if os.path.exists(books_links_csv_path):
        df_book_links.to_csv(books_links_csv_path, mode='a', index=False, header=False)
    else:
        df_book_links.to_csv(books_links_csv_path, mode='w', index=False, header=True)


get_book_links()
export_to_file_books_links(books_urls)
