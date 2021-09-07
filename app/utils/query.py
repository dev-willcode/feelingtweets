from datetime import date
from typing import List


class Query:
    search: List[str]
    date_start: str
    date_end: str
    language: str
    interval_day: int

    def __init__(self,
                 search: List[str],
                 date_start=date.today().__str__(),
                 date_end=date.today().__str__(),
                 language='es',
                 interval_day=1
                 ):
        self.search = search
        self.date_start = date_start
        self.date_end = date_end
        self.language = language
        self.interval_day = interval_day
