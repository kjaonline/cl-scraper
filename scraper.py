import pprint
from classes.listings import Listing

craigslist_page = 'https://jacksonville.craigslist.org/search/mca?query=cruiser&purveyor-input=all';

listing = Listing(craigslist_page)
print(listing.get_listings())