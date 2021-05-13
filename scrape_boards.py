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
LEADERBOARDS = ['STD', 'WLD', 'BG']

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


#print("running....")
def get_season(season):
    with open("./json/" + season + ".json", "w") as f:
        if int(season) >= 73:
            json.dump(format_post_bg(season), f)
        else:
            json.dump(format_pre_bg(season), f)
    return