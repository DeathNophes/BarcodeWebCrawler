# Gathering the barcodes from the books' links

# Importing necessary modules
from helpers import books_links_csv_path, books_barcodes_csv_path
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# Read the csv file and create a list
book_links_data = pd.read_csv(books_links_csv_path)
book_links_list = list(book_links_data['urls'])

# Create a set for uniqueness check
current_books_barcodes = pd.read_csv(books_barcodes_csv_path)
barcodes = set(current_books_barcodes['ISBN'])

# Creating a dictionary to store all the gathered barcodes
data = {'ISBN': []}


def iterate_through_books_links():
    # Iterate through all books' links and get their barcodes if they exist
    # Using time.sleep() to respect robots.txt

    for link in book_links_list:
        html_content = requests.get(link).text
        flag = False

        # Create an instance of BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')

        characteristics = soup.find_all('table', class_='stylized attributes')
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
    # Create a DataFrame with the data
    # Append the data to the csv file

    df = pd.DataFrame.from_dict(required_data, orient='columns')
    df.to_csv(books_barcodes_csv_path, mode='a', index=False, header=False)


iterate_through_books_links()
export_to_file(data)
