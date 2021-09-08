
from pandas.core.frame import DataFrame
from utils.query import Query
from utils.writter import FileWritter
from collector.collectorConfig import CollectorConfig
from twscrapper.scrapper import scrap
import os


class TweetCollector:
    __writer: FileWritter

    def __init__(self, config: CollectorConfig):
        self.__writer = FileWritter(config)

    def __generate_file_name(self, query: Query):
        name = 'tweets_collected_at_'
        name += query.date_start

        if(query.date_end):
            name += "_until_" + query.date_end
        return name

    def collect(self, query: Query, save_file=False):
        print("Start collecting....")
        print("query = " + query.get_search_str() +
              " since: " + query.date_start +
              " until: " + query.date_end)

        tweets = scrap(words=query.get_search_str(),
                       since=query.date_start,
                       until=query.date_end,
                       lang=query.language,
                       interval=query.interval_day,
                       limit=query.limit_tweets)
        if save_file:
            self.__write_results(tweets, query)
        return tweets

    def __write_results(self, data: DataFrame, query: Query):
        file_name = self.__generate_file_name(query)
        self.__writer.save_collected_file(file_name, data)
