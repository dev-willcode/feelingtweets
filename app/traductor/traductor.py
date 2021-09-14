from utils.writter import FileWritter
from pandas.core.frame import DataFrame
from collector.collectorConfig import CollectorConfig
from googletrans import Translator
import pandas as pd


class Traductor:
    __config: CollectorConfig
    __writter: FileWritter
    __translator: Translator
    __TRADUCED_COLUMNS = ["original", "traduced"]

    def __init__(self, config: CollectorConfig):
        self.__config = config
        self.__writter = FileWritter(config)
        self.__translator = Translator()

    def traduce(self, data: DataFrame, save_file=False):
        print("Start traducing....")
        traduced_data = self.__traduce_data(data)
        if save_file and traduced_data is not None:
            self.__write_results(traduced_data)
        print("Traduce process finished.")
        return traduced_data

    def traduce_file(self, path: str, save_file=False):
        print("Start traducing....")
        data = pd.read_csv(path)
        traduced_data = self.__traduce_data(data)
        if save_file and traduced_data is not None:
            self.__write_results(traduced_data)
        print("Traduce process finished.")
        return traduced_data

    def __write_results(self, data: DataFrame):
        file_name = self.__generate_file_name()
        self.__writter.save_traduced_file(file_name, data)
        return file_name

    def __generate_file_name(self):
        return 'traduced_data'

    def __traduce_data(self, data: DataFrame):
        try:
            if data.empty:
                raise ValueError("Translator: Empty data!")
            traduced_data: list[list[str]] = []
            for tweet in data[self.__config.cleaner_column]:
                traduced_tweet = self.__translator.translate(
                    tweet, src=self.__config.input_collect_language,
                    dest=self.__config.output_traduce_language)
                traduced_data.append([tweet, traduced_tweet.text])
            df = DataFrame(traduced_data, columns=self.__TRADUCED_COLUMNS)
            return df
        except ValueError as e:
            print(e)
