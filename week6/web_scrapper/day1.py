from bs4 import BeautifulSoup
import requests
import re

base_url = "https://www.billboard.com/charts/hot-100"
final_data = []


def item_scraper(element):
    song_data = {
        'rank': int(re.sub('[^0-9]', '', element.find('li').text.strip())),
        'singer': element.find('h3').text.strip(),
        'song_name': element.find('span', {'class', 'a-font-primary-s'}).text.strip(),
    }
    # print(info_container.text)
    final_data.append(song_data)


def page_scraper(input_url):
    request_data = requests.get(input_url)
    page_dom = BeautifulSoup(request_data.text, 'html.parser')
    music_containers = page_dom.findAll('div', {'class': 'o-chart-results-list-row-container'})
    for music_container in music_containers:
        item_scraper(music_container)


page_scraper(base_url)

print(final_data)
