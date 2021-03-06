from pandas.core.frame import DataFrame
from feelingtweets.utils.config import Config
from feelingtweets.utils.writter import FileWritter
import re as regex
import pandas as pd


class Cleaner:
    __config: Config
    __writer: FileWritter

    def __init__(self, config: Config):
        self.__config = config
        self.__writer = FileWritter(config)

    def clean(self, data: DataFrame, save_file=False):
        print("Start cleaning....")
        clean_data = self.__clean_data(data)
        if save_file and clean_data is not None:
            self.__write_results(clean_data)
        print("Clean process finished.")
        return clean_data

    def clean_file(self, path: str, save_file=False):
        print("Start cleaning....")
        data = pd.read_csv(path)
        clean_data = self.__clean_data(data)
        if save_file:
            self.__write_results(clean_data)
        print("Clean process finished.")
        return clean_data

    def __write_results(self, data: DataFrame):
        file_name = self.__generate_file_name()
        self.__writer.save_cleaned_file(file_name, data)
        return file_name

    def __generate_file_name(self):
        return 'cleaned_data'

    def __clean_data(self, data: DataFrame):
        filtered_data = []
        try:
            if data.empty:
                raise ValueError("Translator: Empty data!")
            for tweet in data[self.__config.collector_column]:
                processed = self.__convert_lowercase(tweet)
                processed = self.__clean_mentions(processed)
                processed = self.__clean_links(processed)
                processed = self.__clean_specials_characters(processed)
                processed = self.__clean_individual_characters(processed)
                processed = self.__clean_first_individual_character(processed)
                processed = self.__clean_b_prefix(processed)
                processed = self.__clean_hashtag(processed)
                processed = self.__clean_numbers(processed)
                processed = self.__clean_whitespaces(processed)
                # check that result is not empty tweet
                if processed:
                    filtered_data.append(processed)

            df = DataFrame(filtered_data, columns=[
                           self.__config.cleaner_column])
            df = df.dropna()
            df = df.drop_duplicates(subset=[self.__config.cleaner_column])
            return df
        except ValueError as e:
            print(e)

    def __convert_lowercase(self, text: str):
        return text.lower()

    def __clean_links(self, text: str):
        regex_links = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        return regex.sub(regex_links, " ", text)

    def __clean_mentions(self, text: str):
        regex_menciones = "@[\w\-]+"
        return regex.sub(regex_menciones, " ", text)

    def __clean_hashtag(self, text: str):
        regex_hashtag = "#[\w\-]+"
        return regex.sub(regex_hashtag, " ", text)

    def __clean_specials_characters(self, text: str):
        regex_caracteres_especiales = r"\W"
        return regex.sub(regex_caracteres_especiales, " ", text)

    def __clean_individual_characters(self, text: str):
        regex_caracter_individual = r"\s+[a-zA-Z]\s+"
        return regex.sub(regex_caracter_individual, " ", text)

    def __clean_first_individual_character(self, text: str):
        regex_caracter_individual_inicio = r"\^[a-zA-Z]\s+"
        return regex.sub(regex_caracter_individual_inicio, " ", text)

    def __clean_whitespaces(self, text: str):
        regex_varios_espacios = r"\s+"
        result = regex.sub(regex_varios_espacios, " ", text)
        return result.lstrip()

    def __clean_b_prefix(self, text: str):
        regex_prefijo_b = r"^b\s+"
        return regex.sub(regex_prefijo_b, " ", text)

    def __clean_numbers(self, text: str):
        regex_numeros = "[0-9]+"
        return regex.sub(regex_numeros, " ", text)
