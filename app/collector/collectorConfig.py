from datetime import date
from os import path


class CollectorConfig:
    output_folder: str
    output_folder_collected: str
    output_folder_cleaned: str
    output_folder_analized: str

    def __init__(self,
                 output_folder="C:\\Users\\willy\\Documents\\Analisys",
                 output_folder_collected="collected",
                 output_folder_cleaned="cleaned",
                 output_folder_analized="analized",
                 ):
        self.output_folder = output_folder
        self.output_folder_collected = output_folder_collected
        self.output_folder_cleaned = output_folder_cleaned
        self.output_folder_analized = output_folder_analized
