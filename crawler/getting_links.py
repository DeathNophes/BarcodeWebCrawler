# Getting the links to the catalogue pages

# Importing necessary modules
from bs4 import BeautifulSoup
from helpers import pages_links_books_csv_path, books_links_csv_path
import pandas as pd
import requests
import time


def get_pages_links():

    # Create a dictionary to store the links
    data = {'Links': []}

    # This is the total number of pages in the store catalogue
    total_pages_with_books = 1000

    # The whole idea here is to get the links to all the pages with books in the store
    for i in range(2, total_pages_with_books):
        link = f"url_page_of_the_website_catalogue"
        data['Links'].append(link)

    # Create a DataFrame with the data and write it in the file
    df_pages = pd.DataFrame.from_dict(data, orient='columns')
    df_pages.to_csv(pages_links_books_csv_path, mode='w', index=False, header=True)


def export_to_file_book_links(data):
    # Append the data to the csv file

    df_book_links = pd.DataFrame.from_dict(data, orient='columns')
    df_book_links.to_csv(books_links_csv_path, mode='a', index=False, header=False)


def get_book_links():

    current_pages = pd.read_csv(pages_links_books_csv_path)
    urls = list(current_pages['Links'])

    urls_data = {'urls': []}

    for url in urls[:1]:
        html_text = requests.get(url).text

        soup = BeautifulSoup(html_text, 'lxml')
        books = soup.find_all('div', class_='col-xs-3 five-on-a-row')

        for book in books:

            products = book.find_all('a', class_='product-box')

            for product in products:
                href = product.get('href')
                urls_data['urls'].append(href)

        time.sleep(1)

    export_to_file_book_links(urls_data)
