from __future__ import unicode_literals
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date, timedelta
from subprocess import call
import sys
import youtube_dl


def soupify(url):
    chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--window-position=-0,0");
    # chrome_options.add_argument("--window-size=0,0")
    # driver.set_window_position(0, 0)
    # driver.set_window_size(0,0)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    driver.get(url)

    data = driver.page_source
    driver.close()

    return BeautifulSoup(data,'lxml')

def find_days_games(soup, date):
    game_sections = soupify(url).findAll('section', {'class': 'tile'})
    correct_urls = []
    base_url = 'http://www.nba.com'
    for game in game_sections:
        if date in game['data-video-id']:
            correct_urls.append(base_url + game['data-video-id'])
    return correct_urls


def my_hook(d):
    if d['status'] == 'finished':
        print('Finished downloading %s' % d['filename'])
        try:
            if sys.argv[2]:
                call('open "%s"' % d['filename'], shell=True)
        except:
            print('\n')

def download_games(game_urls):
    ydl_opts = {
    "forcetitle": True,
    "quiet": True,
    "outtmpl": "%(title)s.%(ext)s",
    "progress_hooks": [my_hook],
    "nooverwrites": True,
    "no_warnings": True,
    "ignoreerrors": True
    }
    for game_url in game_urls:
        meta = youtube_dl.YoutubeDL(ydl_opts).extract_info(game_url, download=False)
        print 'upload date : %s' %(meta['upload_date'])
        print 'id          : %s' %(meta['id'])
        print 'format      : %s' %(meta['format'])
        print 'duration    : %s' %(meta['duration'])
        print 'title       : %s' %(meta['title'])
        print 'description : %s' %(meta['description'])
        print '-----------------------------------------'
    youtube_dl.YoutubeDL(ydl_opts).download(game_urls)



if __name__ == '__main__':
    print(sys.argv)
    try:
        days_ago = int(sys.argv[1])
    except:
        days_ago = 1
    date = (date.today() - timedelta(days_ago)).strftime('%Y/%m/%d')
    url = 'http://www.nba.com/video/gamerecaps#/'
    soup = soupify(url)
    game_urls = find_days_games(soup, date)
    download_games(game_urls)
    call("killall chromedriver", shell=True)
    exit()








