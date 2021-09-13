from utils.writter import FileWritter
from pandas.core.frame import DataFrame
from collector.collectorConfig import CollectorConfig
from pygoogletranslation import Translator


class Traductor:
    __config: CollectorConfig
    __writer: FileWritter
    __translator: Translator

    def __init__(self, config: CollectorConfig):
        self.__config = config
        self.__translator = Translator()

    def traduce(self, data: DataFrame, save_file=False):
        print("Start traducing....")
        clean_data = self.__traduce_data(data)
        if save_file:
            self.__write_results(clean_data)
        print("Traduce process finished.")
        return clean_data

    def __write_results(self, data: DataFrame):
        file_name = self.__generate_file_name()
        self.__writer.save_traduced_file(file_name, data)
        return file_name

    def __generate_file_name(self):
        return 'traduced_data'

    def __traduce_data(self, data: DataFrame):
        traduced_data: list[list[str]] = []
        for tweet in data[self.__config.cleaner_column]:
            traduced_tweet = self.__translator.translate(
                tweet, self.__config.input_collect_language, self.__config.output_traduce_language)

            traduced_data.append([tweet, traduced_tweet])
        df = DataFrame(traduced_data, columns=[self.__config.cleaner_column])
        return df
