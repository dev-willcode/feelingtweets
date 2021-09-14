from typing import List
from pandas.core.frame import DataFrame
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VaderAnalizer:
    vader = SentimentIntensityAnalyzer()

    def __vader_score(self, sentence):
        return self.vader.polarity_scores(sentence)['compound']

    def analize(self, text_list: List[str]):
        analized_data = []
        for text in text_list:
            score = self.__vader_score(text)
            analized_data.append([text, score])
        return DataFrame(analized_data, columns=["text", "score"])
