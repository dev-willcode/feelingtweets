from datetime import date


class Query:
    search: str
    date_start: str
    date_end: str
    language: str
    interval_day: int
    limit_tweets: int

    def __init__(self,
                 search: str,
                 date_start=date.today().__str__(),
                 date_end=date.today().__str__(),
                 language='es',
                 interval_day=1,
                 limit_tweets=float("inf")
                 ):
        self.search = search
        self.date_start = date_start
        self.date_end = date_end
        self.language = language
        self.interval_day = interval_day
        self.limit_tweets = limit_tweets

    def get_search_query(self):
        return self.search.replace(" ", "%20")
