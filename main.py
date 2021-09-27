import os
import utils
from hltv import get_news_from_soup, get_main_page_soup

news_dir = os.getcwd() + '/news/'

HLTV_NEWS = True

if HLTV_NEWS:

    # Check for hltv news
    hltv_news_file = news_dir + 'hltv.txt'

    # in the file we will keep ids of the news we have sent
    try:
        hltv_news_from_file = open(news_dir+'/hltv.txt', 'r').read().splitlines()
    except:
        hltv_news_from_file = ['hltv-01']

    # get the current news
    hltv_soup = get_main_page_soup()
    hltv_news = get_news_from_soup(hltv_soup)

    articles_to_send = []

    # find the last news that were sent to the phone
    for hltv_article in hltv_news:

        # if this id has been sent already
        if hltv_article['news_id'] in hltv_news_from_file:        
            break
        # this should be before the last id was found
        else:
            articles_to_send.append(hltv_article)

    articles_to_send.reverse()

    # send articles to phone using notifications
    for article in articles_to_send:
        utils.send_phone_notification(values=article)

    # write the send ids to the file
    if len(articles_to_send):
        for article in articles_to_send:
            newest_news_id = article['news_id']
            utils.line_prepender(hltv_news_file, newest_news_id)