# Gathering the barcodes from the books' links

# Importing necessary modules
from helpers import books_links_csv_path, books_barcodes_csv_path
from get_books_links import is_page_url_valid
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import os

# Read the books links file
book_links_data = pd.read_csv(books_links_csv_path)

# We use indexes to access certain range of items
book_links_list = list(book_links_data['urls'])[0:0]

# Creating a dictionary to store all the gathered barcodes
data = {'ISBN': []}

# Create a set for uniqueness check
if os.path.exists(books_barcodes_csv_path):
    current_books_barcodes = pd.read_csv(books_barcodes_csv_path)
    barcodes = set(current_books_barcodes['ISBN'])
else:
    barcodes = set()


def iterate_through_books_links():
    # Iterate through all valid books' links

    for link in book_links_list:
        if not is_page_url_valid(link):
            continue

        html_content = requests.get(link).text
        flag = False

        # Create an instance of BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')

        characteristics = soup.find_all('table', class_='stylized attributes')

        # Iterate through every characteristic to search for the ISBN
        for characteristic in characteristics:
            tables_values = characteristic.find_all('tr')

            for value in tables_values:
                new_list = [i for i in value.text.split('\n') if i != '']

                if new_list[0] == 'ISBN':
                    if new_list[1] not in data['ISBN'] and new_list[1] not in barcodes:
                        data['ISBN'].append(new_list[1])

                    flag = True
                    break

            if flag:
                break

        time.sleep(1)


def export_to_file(required_data):
    # Create a DataFrame
    df = pd.DataFrame.from_dict(required_data, orient='columns')

    # Check if the file exists
    if os.path.exists(books_barcodes_csv_path):
        df.to_csv(books_barcodes_csv_path, mode='a', index=False, header=False)
    else:
        df.to_csv(books_barcodes_csv_path, mode='w', index=False, header=True)


iterate_through_books_links()
export_to_file(data)
