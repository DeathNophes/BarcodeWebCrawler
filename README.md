For this project, I was tasked with creating a Python script 🐍 that automatically gathers all available barcodes from a specific category of an online store 🛒. Following that, I developed a robot 🤖 for automatic data entry, which checks which of the gathered barcodes are missing on another website 🌐. This task was previously done manually, but by automating it, I significantly boosted team efficiency — employee productivity per hour has nearly doubled ⏱️!

How to download and use?
1. Clone the repository to your local machine.

2. Install the required dependencies: `pip install -r requirements.txt`

We scrape the data with BeautifulSoup and handle it using the Pandas library:
In the `data` directory, we store all of our data in `.csv` files.

3. The `get_pages_links.py` file contains the functions that iterate through all the web page numbers and save their URLs inside `page_links_books.csv`.

The `get_books_links.py` file contains the functions to enter each page URL and get the URL of every book on the webpage, storing them inside `books_links.csv`.

The `get_books_barcodes.py` file contains the functionality to parse through every book link inside `books_links.csv` and extract each book's barcode. After going through the validation steps, it saves the valid barcodes into `books_barcodes.csv`.

We check whether the barcodes are already included in our web catalog using Selenium:

The `check_items_from_admin_panel.py` file contains all the functions and logic for checking in the admin panel of the website whether the barcode is in the web catalog. If not, it adds it to the `valid_barcodes_books.txt` file.