import urllib.request
from bs4 import BeautifulSoup

def get_main_page_soup():

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    referer = "https://www.google.com/"
    url = "https://www.hltv.org/"

    req = urllib.request.Request(
        url,
        data=None,
        headers=user_agent
    )

    req.add_header('Referer', referer)

    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_news_from_soup(soup):
    
    news_articles_to_return = []
    news_articles = soup.find_all(class_="newsline article")
    for news in news_articles:
        news_article_dict = {}
        news_article_dict['title'] = 'hltv.org'
        news_article_dict['text'] = news.find(class_='newstext').text
        news_link = news['href']
        news_article_dict['news_id'] = 'hltv-' + news_link.split('/')[2]
        news_article_dict['link'] = 'https://www.hltv.org' + str(news_link)
        news_articles_to_return.append(news_article_dict)

    return news_articles_to_return