from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from selenium import webdriver
import time
import json


REGIONS = ["US", "EU", "AP"]
LEADERBOARDS = ["STD", "WLD", "BG"]
PAGES = [i for i in range(1,9)]
SEASONS= ["73", "72", "71", "70", "69"]


debug = True
if debug:
        SEASONS = ['73', '72']
        REGIONS = ['US', 'EU']
        LEADERBOARDS = ['STD', 'WLD', 'BG']
        PAGES = [1, 2]


def get_request(url):
        return requests.get(url).text


def get_boards(url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        time.sleep(.75)
        html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')

        soup = BeautifulSoup(html, features = 'lxml') 

        ranks = soup.find_all('div', {'class':'Column col-rank'})

        tags = soup.find_all('div', {'class': 'Column col-battletag'})
        lb = dict(zip([tag.text for tag in tags], [rank.text for rank in ranks]))
        return lb


def build(seasonId):
    url = "https://playhearthstone.com/en-us/community/leaderboards/?region={}&leaderboardId={}&seasonId=" + seasonId + "&page={}"
    reg = {"US": {"STD": {}, "WLD": {}, "BG": {}}, "EU": {"STD": {}, "WLD": {}, "BG": {}}, "AP": {"STD": {}, "WLD": {}, "BG": {}}}
    old_reg = {"US": {"STD": {}, "WLD": {}}, "EU": {"STD": {}, "WLD": {}}, "AP": {"STD": {}, "WLD": {}}}

    if int(seasonId) <= 72:
        for r in REGIONS:
            for l in ['STD', 'WLD']:
                for p in PAGES:
                    old_reg[r][l].update(get_boards(url.format(r,l,p)))
        return old_reg

    else:
        for r in REGIONS:
            for l in LEADERBOARDS:
                for p in PAGES:
                    reg[r][l].update(get_boards(url.format(r, l ,p)))

    return reg


def write_to_json(season, reg):
    with open("./json/" + season + '.txt') as f:
        json.dump(reg, f)


def build_all():
    for s in SEASONS:
        write_to_json(s, build(s))


build_all()
print('done')
