from datetime import date


class CollectorConfig:
    output_folder: str
    date_start: date
    date_end: date
    language: str
    interval_day: int

    def __init__(self, output_folder='data',
                 date_start=date.today().__str__(),
                 date_end=date.today().__str__(),
                 language='es',
                 interval_days=1):
        self.output_folder = output_folder
        self.date_start = date_start
        self.date_end = date_end
        self.language = language
        self.interval_day = interval_days
