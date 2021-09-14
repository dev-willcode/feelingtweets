from scrapper.scrapper import Scrapper
from pandas.core.frame import DataFrame
from utils.query import Query
from utils.writter import FileWritter
from utils.config import Config


class TweetCollector:
    __writer: FileWritter
    __scrapper: Scrapper

    def __init__(self, config: Config):
        self.__writer = FileWritter(config)
        self.__scrapper = Scrapper(config)

    def __generate_file_name(self, query: Query):
        name = 'tweets_collected_at_'
        name += query.date_start

        if(query.date_end):
            name += "_until_" + query.date_end
        return name

    def collect(self, query: Query, save_file=False):
        print("Start collecting....")
        print("query = " + query.search +
              " since: " + query.date_start +
              " until: " + query.date_end)

        tweets = self.__scrapper.scrap(query)
        if save_file and tweets is not None:
            self.__write_results(tweets, query)
        return tweets

    def __write_results(self, data: DataFrame, query: Query):
        file_name = self.__generate_file_name(query)
        self.__writer.save_collected_file(file_name, data)
