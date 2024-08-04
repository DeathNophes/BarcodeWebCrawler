# Checking which book is already uploaded into the website and which is not

# Importing necessary modules
from selenium.common import NoSuchElementException
from crawler.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers import admin_panel_link, valid_barcodes_file_path, books_barcodes_csv_path
import pandas as pd
import time

# Reading the csv file which holds the barcodes
books_barcodes = pd.read_csv(books_barcodes_csv_path)

# We use indexes to access certain range of barcodes
books_list = list(books_barcodes['ISBN'])[0:0]

# Creating a dictionary where we will store the barcodes that have not yet been uploaded
data = {'ISBN': []}


def enter_the_admin_panel():
    # Opening the admin panel of the store and entering the email and password

    driver.get(admin_panel_link)

    email_bar = driver.find_element(By.ID, "email")
    email_bar.click()
    email_bar.send_keys('email')

    password_bar = driver.find_element(By.ID, "password")
    password_bar.click()
    password_bar.send_keys("password")

    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    time.sleep(2)


def iterate_through_barcodes():
    # Iterate through the barcodes
    # If the barcode is not shown in the admin panel then we keep it

    for book in books_list:
        search_bar = driver.find_element(By.ID, "search-bar")
        search_bar.click()

        search_bar.send_keys(Keys.CONTROL, "a")
        search_bar.send_keys(Keys.DELETE)

        time.sleep(2)

        search_bar.send_keys(book)
        search_bar.send_keys(Keys.ENTER)

        if not check_is_barcode_in_database():
            data['ISBN'].append(book)

        time.sleep(1)


def check_is_barcode_in_database():
    # If the barcode has been uploaded returns True else None

    try:
        result = driver.find_element(By.XPATH, "xpath")
    except NoSuchElementException:
        return True


def export_to_file():
    # Appending every barcode into text file

    with open(valid_barcodes_file_path, "a") as file:
        for barcode in data['ISBN']:
            file.write(barcode + '\n')


# enter_the_admin_panel()
# iterate_through_barcodes()
# export_to_file()
