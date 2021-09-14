from pandas.core.frame import DataFrame
from feelingtweets.utils.query import Query
from feelingtweets.utils.config import Config
from twint import run, Config, storage


class Scrapper:
    __config: Config

    def __init__(self, config: Config):
        self.__config = config

    def print(self, arg):
        print(arg)

    def scrap(self, query: Query):
        try:
            params = Config()
            params.Limit = query.limit_tweets
            params.Search = query.search
            params.Lang = self.__config.input_collect_language
            params.Pandas = True
            params.Since = query.date_start
            params.Until = query.date_end
            params.TwitterSearch = True
            run.Search(params)
            result: DataFrame = storage.panda.Tweets_df
            if result.empty:
                raise ValueError("Scrapper: Empty results!")
            return result
        except ValueError as e:
            print(e)
