from datetime import date
from os import path


class CollectorConfig:
    output_folder: str
    output_folder_collected: str
    date_start: date
    date_end: date
    language: str
    interval_day: int

    def __init__(self,
                 date_start=date.today().__str__(),
                 date_end=date.today().__str__(),
                 language='es',
                 interval_days=1,
                 output_folder="C:\\Users\\willy\\Documents\\Analisys",
                 output_folder_collected="collected",
                 output_folder_cleaned="cleaned",
                 output_folder_analized="analized",
                 ):
        self.output_folder = output_folder
        self.date_start = date_start
        self.date_end = date_end
        self.language = language
        self.interval_day = interval_days
        self.output_folder_collected = output_folder_collected
        self.output_folder_cleaned = output_folder_cleaned
        self.output_folder_analized = output_folder_analized
