
import json
from bs4 import BeautifulSoup
import requests

URL = 'https://galaxiaestates.com/property-search-results/page/1/?property-id&filter_search_action%5B0%5D&filter_search_type%5B0%5D=apartments&advanced_city=limassol&advanced_area&bedrooms&enter-min-price&enter-max-price=1300&submit=Search%20Properties&wpestate_regular_search_nonce=492ae43431&_wp_http_referer=%2Flimassol-properties-for-rent%2Fapartments-rent-limassol%2F'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',
    'accept': '*/*'
}
HOST = ''
def getnsoup_content(url, params=None):
    r = requests.get(url, params=params, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    property_list = soup.find_all('div', class_='property_unit_type1')
    print(property_list)
if __name__ == '__main__':
    getnsoup_content(URL)

