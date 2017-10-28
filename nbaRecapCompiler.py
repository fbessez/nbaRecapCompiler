from __future__ import unicode_literals
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date, timedelta
# from time import sleep
from subprocess import call
import sys
import youtube_dl

def soupify(url):
	driver = webdriver.PhantomJS()
	driver.get(url)

	data = driver.page_source
	driver.close()

	return BeautifulSoup(data,'lxml')

def find_days_games(soup, days_ago=1):
	game_sections = soupify(url).findAll('section', {'class': 'tile'})
	correct_urls = []
	base_url = 'http://www.nba.com'
	yesterdays_date = (date.today() - timedelta(days_ago)).strftime('%Y/%m/%d')
	for game in game_sections:
		if yesterdays_date in game['data-video-id']:
			correct_urls.append(base_url + game['data-video-id'])
	return correct_urls


def download_games(game_urls):
	ydl_opts = {}
	youtube_dl.YoutubeDL(ydl_opts).download(game_urls)


if __name__ == '__main__':
	try:
		days_ago = int(sys.argv[1])
	except:
		days_ago = 1
	url = 'http://www.nba.com/video/gamerecaps#/'
	soup = soupify(url)
	game_urls = find_days_games(soup, days_ago)
	download_games(game_urls)
	call('open *.mp4', shell=True)
	# call('rm *.mp4', shell=True)












