import datetime
from time import sleep
import random
import pandas as pd

from .utils import init_driver, log_search_page, keep_scroling


def scrap(since, until, words, interval, lang,
          limit, headless=True, proxy=None):

    # columns header
    columns = ['UserScreenName', 'UserName', 'Timestamp', 'Text',
               'Embedded_text', 'Emojis', 'Comments', 'Likes', 'Retweets', 'Tweet URL']
    data = []
    tweet_ids = set()
    until_local = datetime.datetime.strptime(
        since, '%Y-%m-%d') + datetime.timedelta(days=interval)
    if until is None:
        until = datetime.date.today().strftime("%Y-%m-%d")
    refresh = 0

    if words:
        if type(words) == str:
            words = words.split("//")

    driver = init_driver(headless, proxy)
    while until_local <= datetime.datetime.strptime(until, '%Y-%m-%d'):
        scroll = 0
        if type(since) != str:
            since = datetime.datetime.strftime(since, '%Y-%m-%d')
        if type(until_local) != str:
            until_local = datetime.datetime.strftime(
                until_local, '%Y-%m-%d')
        log_search_page(driver, since, until_local, lang,  words)
        refresh += 1
        last_position = driver.execute_script("return window.pageYOffset;")
        scrolling = True
        tweet_parsed = 0
        sleep(random.uniform(0.5, 1))
        driver, data, tweet_ids, scrolling, tweet_parsed, scroll, last_position = \
            keep_scroling(driver, data, tweet_ids, scrolling,
                          tweet_parsed, limit, scroll, last_position)
        if type(since) == str:
            since = datetime.datetime.strptime(
                since, '%Y-%m-%d') + datetime.timedelta(days=interval)
        else:
            since = since + datetime.timedelta(days=interval)
        if type(since) != str:
            until_local = datetime.datetime.strptime(
                until_local, '%Y-%m-%d') + datetime.timedelta(days=interval)
        else:
            until_local = until_local + datetime.timedelta(days=interval)

    driver.close()
    data = pd.DataFrame(data, columns=columns)
    return data
