from bs4 import BeautifulSoup
from requests import get

class Listing:

    def __init__(self, url):
       self.url = url

    def get_listings(self):
        listings_array = []
        page_content = get(self.url)
        soup = BeautifulSoup(page_content.text, 'lxml')
        listings = soup.find_all('li', class_='result-row')

        for listing in listings: 
            title = listing.find(class_='result-title').text
            price = listing.find(class_='result-price').text
            listing_data = {
                'price': price,
                'title': title
            }
            listings_array.append(listing_data) 
        return listings_array