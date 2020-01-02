from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from selenium import webdriver
import time

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
        #lb = dict(zip([rank.text for rank in ranks] , [tag.text for tag in tags]))
        lb = dict(zip([tag.text for tag in tags], [rank.text for rank in ranks]))
        return lb

REGIONS = ["US", "EU", "AP"]
LEADERBOARDS = ["STD", "WLD", "BG"]
PAGES = [i for i in range(1,9)]

debug = False
if debug:
        REGIONS = ['US', 'EU']
        LEADERBOARDS = ["STD", "WLD"]
        PAGES = [1, 2]

url = "https://playhearthstone.com/en-us/community/leaderboards/?region={}&leaderboardId={}&seasonId=73&page={}"

reg = {"US": {"STD": {}, "WLD": {}, "BG": {}}, "EU": {"STD": {}, "WLD": {}, "BG": {}}, "AP": {"STD": {}, "WLD": {}, "BG": {}}}

BUILD_NEW = True
if BUILD_NEW:
    for r in REGIONS:
        for l in LEADERBOARDS:
            for p in PAGES:
                reg[r][l].update(get_boards(url.format(r, l ,p)))
                    #else:
                        #reg[r][l].update(get_boards(url.format(r,l,p)))

with open('73.txt' , 'w') as f:
    f.write(str(reg))

#redo things for older seasons
url = "https://playhearthstone.com/en-us/community/leaderboards/?region={}&leaderboardId={}&seasonId={}&page={}"

SEASONS = ["72", "71", "70", "69"]


reg2 = {"72": {"US": {"STD": {}, "WLD": {}}, "EU": {"STD": {}, "WLD": {}}, "AP": {"STD": {}, "WLD": {}}}, "71": {"US": {"STD": {}, "WLD": {}}, "EU": {"STD": {}, "WLD": {}}, "AP": {"STD": {}, "WLD": {}}}, "70": {"US": {"STD": {}, "WLD": {}}, "EU": {"STD": {}, "WLD": {}}, "AP": {"STD": {}, "WLD": {}}}, "69": {"US": {"STD": {}, "WLD": {}}, "EU": {"STD": {}, "WLD": {}}, "AP": {"STD": {}, "WLD": {}}}}

if debug:
    SEASONS = ['72', '71']
    REGIONS = ['US', 'EU']
    LEADERBOARDS = ['STD', 'WLD']
    PAGES = [1, 2]

BUILD_OLD = True
if BUILD_OLD:
    for s in SEASONS:
        for r in REGIONS:
            for l in ["STD", "WLD"]:
                for p in PAGES:
                    reg2[s][r][l].update(get_boards(url.format(r,l,s,p)))

with open ('72717069.txt', 'w') as f:
    f.write(str(reg2))

print('done')
