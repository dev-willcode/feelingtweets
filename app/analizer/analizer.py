from utils.writter import FileWritter
from typing import List
from pandas.core.frame import DataFrame
from collector.collectorConfig import CollectorConfig
from textblob import TextBlob
import pandas as pd


class Analizer():
    __config: CollectorConfig
    __columns: List[str]
    __writer: FileWritter

    def __init__(self, config: CollectorConfig):
        self.__config = config
        self.__writer = FileWritter(config)
        self.__columns = [
            "Text",
            "polarity",
            "subjectivity"
        ]

    def analize(self, data: DataFrame, save_file=False):
        print("Start analizing....")
        analized_data = self.__analize_data(data)
        if save_file:
            self.__write_results(analized_data)
        print("Analize process finished.")
        return analized_data

    def analize_file(self, path: str, save_file=False):
        print("Start analizing....")
        data = self.__writer.read_file(path)
        analized_data = self.__analize_data(data)
        if save_file:
            self.__write_results(analized_data)
        print("Analize process finished.")
        return analized_data

    def __write_results(self, data: DataFrame):
        file_name = self.__generate_file_name()
        self.__writer.save_cleaned_file(file_name, data)
        return file_name

    def analize_file(self, path: str):
        print("Start analizing....")
        namer = FileWritter(self.__config)
        analized_data = self.__analize(path)
        output = namer.__build_folder_path(
            self.__config.output_folder_analized,
            self.__generate_file_name(path), ".csv")
        print("saving analizing results...")
        analized_data.to_csv(output)
        print("saved in: " + output)
        print("Analize process finished.")
        return self.__analize(path)

    def __generate_file_name(self):
        return 'analized_data'

    def scoreText(self, text: str) -> float:
        return TextBlob(text).sentiment

    def __analize(self, path: str):
        data = pd.read_csv(path)
        return self.__analize_data(data)

    def __analize_data(self, data: DataFrame):
        analized_data = []
        for tweet in data[self.__config.cleaner_column]:
            sentiment = self.scoreText(tweet)
            analized_data.append([tweet,
                                  sentiment.polarity,
                                  sentiment.subjectivity])
        return DataFrame(analized_data, columns=self.__columns)
