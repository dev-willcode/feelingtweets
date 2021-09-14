from typing import List
from pandas.core.frame import DataFrame
from textblob import TextBlob


class TextBlobAnalizer:

    def __textblob_score(self, sentence):
        return TextBlob(sentence).sentiment.polarity

    def analize(self, text_list: List[str]):
        analized_data = []
        for text in text_list:
            score = self.__textblob_score(text)
            analized_data.append([text, score])
        return DataFrame(analized_data, columns=["text", "score"])
