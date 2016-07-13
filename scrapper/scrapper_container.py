'''
Created on Jul 13, 2016

@author: andriy
'''

import newspaper
from newspaper import news_pool
from newspaper import Article

class Scrapper(object):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def parse(self):
        raise NotImplementedError()

class NewsPaperScrapper(Scrapper):
    
    def __init__(self, site_urls):
        self.site_urls = site_urls
        self.sites_info = []

    def parse(self):
        '''
        This method parses site_url and returns list with infora
        '''
        built_papers = []
        for site_url in self.site_urls:
            built_papers.append(newspaper.build(site_url,
                                                memoize_articles=False))
        for paper in built_papers:  
            for article in paper.articles:
                print(article.url)
                article_obj = Article(article.url)
                article_obj.download()
                article_obj.parse()
                print(article.url)
                print(article_obj.authors)
                print(article_obj.publish_date)
                print(article_obj.title)