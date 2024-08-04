
pages_links_books_csv_path = '../data/page_links_books.csv'
books_links_csv_path = '../data/books_links.csv'

books_barcodes_csv_path = '../data/books_barcodes.csv'
valid_barcodes_books_file_path = '../data/valid_barcodes_books.txt'

admin_panel_link = ''


def is_page_url_valid(url):
    try:
        response = requests.head(url, timeout=5)
        # Check if the satus code is 200 (OK)
        return response.status_code == 200
    except requests.RequestException:
        return False
