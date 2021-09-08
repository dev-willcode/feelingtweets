import re
from time import sleep
import random
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_data(card):
    """Extract data from tweet card"""

    try:
        username = card.find_element_by_xpath('.//span').text
    except:
        return

    try:
        handle = card.find_element_by_xpath(
            './/span[contains(text(), "@")]').text
    except:
        return

    try:
        postdate = card.find_element_by_xpath(
            './/time').get_attribute('datetime')
    except:
        return

    try:
        text = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    except:
        text = ""

    try:
        embedded = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    except:
        embedded = ""

    #text = comment + embedded

    try:
        reply_cnt = card.find_element_by_xpath(
            './/div[@data-testid="reply"]').text
    except:
        reply_cnt = 0

    try:
        retweet_cnt = card.find_element_by_xpath(
            './/div[@data-testid="retweet"]').text
    except:
        retweet_cnt = 0

    try:
        like_cnt = card.find_element_by_xpath(
            './/div[@data-testid="like"]').text
    except:
        like_cnt = 0

    try:
        promoted = card.find_element_by_xpath(
            './/div[2]/div[2]/[last()]//span').text == "Promoted"
    except:
        promoted = False
    if promoted:
        return

    # get a string of all emojis contained in the tweet
    try:
        emoji_tags = card.find_elements_by_xpath(
            './/img[contains(@src, "emoji")]')
    except:
        return
    emoji_list = []
    for tag in emoji_tags:
        try:
            filename = tag.get_attribute('src')
            emoji = chr(
                int(re.search(r'svg\/([a-z0-9]+)\.svg', filename).group(1), base=16))
        except AttributeError:
            continue
        if emoji:
            emoji_list.append(emoji)
    emojis = ' '.join(emoji_list)

    # tweet url
    try:
        element = card.find_element_by_xpath(
            './/a[contains(@href, "/status/")]')
        tweet_url = element.get_attribute('href')
    except:
        return

    tweet = (username, handle, postdate, text, embedded, emojis,
             reply_cnt, retweet_cnt, like_cnt, tweet_url)
    return tweet


def init_driver(headless=True, proxy=None):
    chromedriver_path = chromedriver_autoinstaller.install()
    options = Options()
    if headless is True:
        options.add_argument('--disable-gpu')
        options.headless = True
    else:
        options.headless = False
    options.add_argument('log-level=3')
    if proxy is not None:
        options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Chrome(
        options=options, executable_path=chromedriver_path)
    driver.set_page_load_timeout(100)
    return driver


def log_search_page(driver, since, until_local, lang,  words):
    if words is not None:
        if len(words) == 1:
            words = "(" + str(''.join(words)) + ")%20"
        else:
            words = "(" + str('%20OR%20'.join(words)) + ")%20"
    else:
        words = ""

    if lang is not None:
        lang = 'lang%3A' + lang
    else:
        lang = ""

    until_local = "until%3A" + until_local + "%20"
    since = "since%3A" + since + "%20"
    path = 'https://twitter.com/search?q=' + words + until_local + \
        since + lang + '&src=typed_query'
    print(path)
    driver.get(path)


def keep_scroling(driver, data, tweet_ids, scrolling, tweet_parsed, limit, scroll, last_position):

    while scrolling and tweet_parsed < limit:
        sleep(random.uniform(0.5, 1.5))
        # get the card of tweets
        page_cards = driver.find_elements_by_xpath(
            '//div[@data-testid="tweet"]')
        for card in page_cards:
            tweet = get_data(card)
            if tweet:
                # check if the tweet is unique
                tweet_id = ''.join(tweet[:-2])
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)

                    tweet_parsed += 1
                    if tweet_parsed >= limit:
                        break
        scroll_attempt = 0
        while tweet_parsed < limit:
            scroll += 1
            sleep(random.uniform(0.5, 1.0))
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
                # end of scroll region
                if scroll_attempt >= 2:
                    scrolling = False
                    break
                else:
                    sleep(random.uniform(0.5, 1.5))  # attempt another scroll
            else:
                last_position = curr_position
                break
    return driver, data, tweet_ids, scrolling, tweet_parsed, scroll, last_position
