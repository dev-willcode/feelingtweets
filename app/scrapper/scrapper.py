from utils.query import Query
from collector.collectorConfig import CollectorConfig
from twint import run, Config, storage


class Scrapper:
    __config: CollectorConfig

    def __init__(self, config: CollectorConfig):
        self.__config = config

    def print(self, arg):
        print(arg)

    def scrap(self, query: Query):
        params = Config()
        params.Limit = query.limit_tweets
        params.Search = query.search
        params.Lang = self.__config.input_collect_language
        params.Pandas = True
        params.Since = query.date_start
        params.Until = query.date_end
        run.Search(params)
        return storage.panda.Tweets_df
