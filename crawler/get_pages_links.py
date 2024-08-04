import pandas as pd

def get_pages_links():

    # Create a dictionary to store the links
    data = {'Links': []}

    # This is the total number of pages in the store catalogue
    total_pages_with_books = 1000

    # The whole idea here is to get the links to all the pages with books in the store
    for i in range(2, total_pages_with_books):
        link = f"url_page_of_the_website_catalogue"
        data['Links'].append(link)

    # Create a DataFrame with the data
    df_pages = pd.DataFrame.from_dict(data, orient='columns')

    # Create / Rewrite the existing file
    df_pages.to_csv(pages_links_books_csv_path, mode='w', index=False, header=True)


# get_pages_links()