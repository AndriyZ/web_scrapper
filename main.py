import newspaper
from newspaper import news_pool
from newspaper import Article
import api
import config

it_ukraine_paper = newspaper.build('http://itukraine.org.ua/en/news',
                                   memoize_articles=False)
vice_paper = newspaper.build('https://news.vice.com/hub/sections',
                             memoize_articles=False)
kuiv_post_paper = newspaper.build('http://www.kyivpost.com',
                                  memoize_articles=False)

api.parse(config.SITE_URLS)
# for article in it_ukraine_paper.articles:
#     print(article.url)
#     article_obj = Article(article.url)
#     article_obj.download()
#     article_obj.parse()
#     print(article.url)
#     print(article_obj.authors)
#     print(article_obj.publish_date)
#     print(article_obj.title)

# for category in vice_paper.category_urls():
#     print(category)
#     category_paper =  newspaper.build(category, memoize_articles=False,MAX_AUTHORS = 10)
#     for article in category_paper.articles:
#         print(article.url)
#         article_obj = Article(article.url)
#         article_obj.download()
#         article_obj.parse()
#         print(article.url)
#         print(article_obj.authors)
#         print(article_obj.publish_date)
#         print(article_obj.title)
    