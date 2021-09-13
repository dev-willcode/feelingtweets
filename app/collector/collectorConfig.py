from datetime import date
from os import path


class CollectorConfig:
    output_folder: str
    output_folder_collected: str
    output_folder_cleaned: str
    output_folder_analized: str
    collector_column: str
    cleaner_column: str
    analizer_column: str
    input_collect_language: str
    output_traduce_language: str

    def __init__(self,
                 output_folder="C:\\Users\\willy\\Documents\\Analisys",
                 output_folder_collected="collected",
                 output_folder_cleaned="cleaned",
                 output_folder_analized="analized",
                 collector_column="tweet",
                 cleaner_column="Text",
                 analizer_column="Text",
                 input_collect_language="es",
                 output_traduce_language="en",
                 ):
        self.output_folder = output_folder
        self.output_folder_collected = output_folder_collected
        self.output_folder_cleaned = output_folder_cleaned
        self.output_folder_analized = output_folder_analized
        self.collector_column = collector_column
        self.cleaner_column = cleaner_column
        self.analizer_column = analizer_column
        self.input_collect_language = input_collect_language
        self.output_traduce_language = output_traduce_language
