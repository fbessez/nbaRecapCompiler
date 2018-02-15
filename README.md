# NBA Recap Compiler

NBA Recap Compiler is a simple script that scrapes the NBA homepage for .swf links to a given night's NBA game recaps. It then uses youtube_dl to download them to your current directory and then opens it. I created this script because it was getting incredibly redundant to navigate to each video link every morning. Now, one click and they are running on my local machine (with no ads!).

## Getting Started

All you need to do is run: ```python2.7 nbaRecapCompiler.py <number_of_days_ago_you_want_highlights_from> ```

### Prerequisites

[youtube-dl](https://rg3.github.io/youtube-dl/) & 
[beautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Authors

* **Fabien Bessez** -- [fbessez](https://github.com/fbessez)

## Acknowledgments

* Thank you [youtube-dl](https://rg3.github.io/youtube-dl/)
* Thank you [beautifulSoup](https://www.crummy.com/software/BeautifulSoup/)


## Set up

`sudo pip install BeautifulSoup4 && sudo pip install selenium && sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && sudo chmod a+rx /usr/local/bin/youtube-dl && sudo pip install lxml && brew install ffmpeg`

Then install ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

