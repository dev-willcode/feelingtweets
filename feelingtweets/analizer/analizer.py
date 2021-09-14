from .vader_analizer import VaderAnalizer
from .textblob_analizer import TextBlobAnalizer
from typing import List
from pandas.core.frame import DataFrame
import pandas as pd


class Analizer():
    __textblob_module: TextBlobAnalizer
    __vader_module: VaderAnalizer

    def __init__(self):
        self.__textblob_module = TextBlobAnalizer()
        self.__vader_module = VaderAnalizer()

    def analize(self, data: List[str]):
        textblob = self.analize_with_textblob(data)
        vader = self.analize_with_vader(data)
        result = DataFrame()
        result["text"] = data
        result["textblob_score"] = pd.Series(textblob["score"])
        result["vader_score"] = pd.Series(vader["score"])
        return result

    def analize_with_textblob(self, data: List[str]):
        return self.__textblob_module.analize(data)

    def analize_with_vader(self, data: List[str]):
        return self.__vader_module.analize(data)
