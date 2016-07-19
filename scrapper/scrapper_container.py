'''
Created on Jul 13, 2016

@author: andriy
'''

import newspaper
from newspaper import Article
import datetime
import pytz
import traceback
import logger
logger = logger.get_logger()

class Scrapper(object):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def parse(self):
        raise NotImplementedError()

class NewsPaperScrapper(Scrapper):
    
    def __init__(self, site_urls, not_older):
        self.site_urls = site_urls
        self.sites_info = []
        self.built_newspapers = []
        self.not_older = not_older

    def parse(self):
        '''
        This method parses site_url and returns list with information
        '''
        self.build_newspaper()
        for paper in self.built_newspapers:
            logger.info('Parse articles in {0}'.format(paper.url))
            for article in paper.articles:
                article_obj = Article(article.url)
                try:
                    article_obj.download()
                    article_obj.parse()

                    if self.article_valid(article_obj):
                        self.sites_info.append([article_obj.title,
                                                article_obj.publish_date,
                                                article_obj.authors,
                                                article_obj.text,
                                                article_obj.url])
                except Exception:
                    logger.error('article is not parsed {0}'.format(article.url))
        return self.sites_info

    def build_newspaper(self):
        '''
        This method builds newspaper using their url and newspaper library
        '''
        for site_url in self.site_urls:
            self.built_newspapers.append(newspaper.build(site_url,
                                                       memoize_articles=False))
    
    def article_valid(self, article):
        '''
        This method checks if article is valid.
        i.e if this artcile has title, authors, pubish_date, article_text, and
        article url. Also this method checks if current article is not older
        then 2 days.
        '''
        
        valid = False
        article_has_date = (True if article.publish_date else False)
        if article_has_date:
            if isinstance(article.publish_date, datetime.datetime):
                article_date = article.publish_date.replace(tzinfo=pytz.utc)
                if ((datetime.datetime.now(tz=pytz.utc)-article_date).days<= 2):
                    valid = True
        return valid
        