import json
from os import chdir, system
from os import walk
from os.path import curdir
from os.path import pardir
from urllib.parse import urlencode
from utllib.request import urlopen, Requests
import requests
import ssl
from bs4 import BeautifulSoup
from directory import createDirectory

ssl._create_default_https_context = ssl._create_unverified_context

GOOGLEIMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
WALLPAPERSCRAFT = 'https://wallpaperscraft.com/search/keywords?'
userAgent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
FX = {
    1: 'search_for_image',
    2: 'download_wallpapers_1080p',
    3: 'view_images_directory',
    4: 'set_directory',
    5: 'quit',
}

def search_for_image():
    data = input("enter data to donwload ")
    searchQuery = {'q': data}
    search = urlencode(searchQuery)
    print(search)
    g = GOOGLEIMAGE + search
