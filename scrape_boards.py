from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import json

def get_request(url):
    return requests.get(url).text


driver = webdriver.PhantomJS()
def get_boards(url):
    driver.get(url)
    # time.sleep(2)
    # html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
    #
    # soup = BeautifulSoup(html, features='lxml')
    #
    # ranks = soup.find_all('div', {'class': 'Column col-rank'})
    # tags = soup.find_all('div', {'class': 'Column col-battletag'})
    # print([t.text for t in tags])
    #
    # lb = dict(zip([tag.text for tag in tags], [rank.text for rank in ranks]))

    rows = driver.execute_script("""
      return JSON.parse(document.body.innerText).leaderboard.rows.reduce(function(acc, o){
        acc[o.accountid] = o.rank
        return acc
      }, {})
    """)

    return rows


url = 'https://playhearthstone.com/en-us/api/community/leaderboardsData?region={}&leaderboardId={}&seasonId={}'


REGIONS = ['US', 'EU', 'AP']
LEADERBOARDS = ['STD', 'WLD', 'BG']
#PAGES = [i for i in range(1,9)]

SEASONS = ['76', '75', '74', '73', '72', '71', '70', '69']

debug = False
if debug:
    SEASONS = ['73', '72']
    REGIONS = ['US', 'EU']
    LEADERBOARDS = ['STD', 'WLD', 'BG']
    #PAGES = ['1', '2', '3']

def format_post_bg(SEASON):
    reg = {"US": {"STD": {}, "WLD": {}, "BG": {}},
           "EU": {"STD": {}, "WLD": {}, "BG": {}},
           "AP": {"STD": {}, "WLD": {}, "BG": {}}}

    for r in REGIONS:
        for l in LEADERBOARDS:
            formatted_url = url.format(r, l, SEASON)
            reg[r][l] = get_boards(formatted_url)

    return reg


def format_pre_bg(SEASON):
    reg = {"US": {"STD": {}, "WLD": {}},
           "EU": {"STD": {}, "WLD": {}},
           "AP": {"STD": {}, "WLD": {}}}

    LEADERBOARDS = ['STD', 'WLD']

    for r in REGIONS:
        for l in LEADERBOARDS:
            formatted_url = url.format(r, l, SEASON)
            reg[r][l] = get_boards(formatted_url)

    return reg


print("running....")
for s in SEASONS:
    with open("./json/" + s + ".json", "w") as f:
        if int(s) >= 73:
            json.dump(format_post_bg(s), f)
        else:
            json.dump(format_pre_bg(s), f)
