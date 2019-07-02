# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs

class SpiegeonlinearchiveSpider(scrapy.Spider):
    name = 'spiegeOnlineArchive'
    start_urls = ['https://www.spiegel.de/nachrichtenarchiv/']

    def parse(self, response):
        soup = bs(response.text, 'html.parser')
        div = soup.find('div', 'column-wide')
        newsOfTheDay = div.find_all('li')
        for news in newsOfTheDay:
            print(news.find('a')['href'])
            for s in news.find_all('span'):
                print(s.contents)
