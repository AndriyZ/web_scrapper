'''
Created on Jul 13, 2016

@author: andriy
'''
from scrapper.scrapper_container import NewsPaperScrapper


def parse(sites_urls, not_older):
    '''
    This function runs parse of sites from sites_url
    :param list sites_urls - list with sites urls
    :return list sites_information
    '''
    scrapper = NewsPaperScrapper(sites_urls, not_older)
    scrapper.parse()
    return scrapper.sites_info
    