from pandas.core.frame import DataFrame
from collector.collectorConfig import CollectorConfig
from os import path
import os


class FileWritter:
    __config: CollectorConfig
    __EXTENSION = ".csv"

    def __init__(self, config: CollectorConfig):
        self.__config = config

    def save_analized_file(self, file_name: str,  data: DataFrame):
        path = self.__build_folder_path(
            self.__config.output_folder_analized, file_name)
        print("saving results...")
        data.to_csv(path)
        print("saved in: " + path)

    def save_collected_file(self, file_name: str,  data: DataFrame):
        path = self.__build_folder_path(
            self.__config.output_folder_collected, file_name)
        print("saving results...")
        data.to_csv(path)
        print("saved in: " + path)

    def save_cleaned_file(self, file_name: str,  data: DataFrame):
        path = self.__build_folder_path(
            self.__config.output_folder_cleaned, file_name)
        print("saving results...")
        data.to_csv(path)
        print("saved in: " + path)

    def save_traduced_file(self, file_name: str,  data: DataFrame):
        path = self.__build_folder_path(
            self.__config.output_folder_traduced, file_name)
        print("saving results...")
        data.to_csv(path)
        print("saved in: " + path)

    def __build_folder_path(self, folder: str,
                            file_name: str, file_number: int = 0):
        main_path = self.__config.output_folder
        if(not path.exists(main_path)):
            # path por defecto, en el home directory.
            main_path = path.join(path.expanduser("~"), "Analysis")

        dir_path = path.join(main_path, folder)
        if(not path.exists(dir_path)):
            self.create_subfolder(dir_path)

        output_path = path.join(dir_path,
                                self.append_file_number
                                (file_name, file_number)) + self.__EXTENSION

        if(path.exists(output_path)):
            return self.__build_folder_path(folder, file_name, file_number+1)
        return output_path

    def create_subfolder(self, folder: str):
        os.makedirs(folder)

    def append_file_number(self, filename: str, number: int):
        if(number == 0):
            return filename
        return filename + "(" + number.__str__() + ")"
