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
    rows = driver.execute_script("""
      return JSON.parse(document.body.innerText).leaderboard.rows.reduce(function(acc, o){
        acc[o.accountid] = o.rank
        return acc
      }, {})
    """)

    return rows


url = 'https://playhearthstone.com/en-us/api/community/leaderboardsData?region={}&leaderboardId={}&seasonId={}'


REGIONS = ['US', 'EU', 'AP']
LEADERBOARDS = ['STD', 'WLD', 'BG', 'CLS']


PRE_BG = {"US": {"STD": {}, "WLD": {}},
           "EU": {"STD": {}, "WLD": {}},
           "AP": {"STD": {}, "WLD": {}}}

PRE_BG_BOARDS = ['STD', 'WLD']

POST_BG= {"US": {"STD": {}, "WLD": {}, "BG": {}},
           "EU": {"STD": {}, "WLD": {}, "BG": {}},
           "AP": {"STD": {}, "WLD": {}, "BG": {}}}

POST_BG_BOARDS = ['STD', 'WLD', 'BG']

POST_CLS = {"US": {"STD": {}, "WLD": {}, "BG": {}, "CLS": {}},
           "EU": {"STD": {}, "WLD": {}, "BG": {}, "CLS": {}},
           "AP": {"STD": {}, "WLD": {}, "BG": {}}, "CLS": {}}

POST_CLS_BOARDS = ['STD', 'WLD', 'BG', 'CLS']

def format_scrape(season, result_dict, boards):
    reg = result_dict

    for r in REGIONS:
        for l in boards:
            formatted_url = url.format(r, l, season)
            reg[r][l] = get_boards(formatted_url)

    return reg


#print("running....")
def get_season(season):
    with open("./json/" + season + ".json", "w") as f:
        if int(season) >= 89:
            json.dump(format_scrape(season, POST_CLS, POST_CLS_BOARDS), f)
        elif (int(season) >= 73) & (int(season) < 89):
            json.dump(format_scrape(season, POST_BG, POST_BG_BOARDS), f)
        else:
            json.dump(format_scrape(season, PRE_BG, PRE_BG_BOARDS), f)
    return