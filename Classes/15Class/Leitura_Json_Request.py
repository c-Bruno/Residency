from bs4 import BeautifulSoup
import requests

requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(r.text, 'html.parse')