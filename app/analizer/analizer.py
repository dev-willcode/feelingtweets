from textblob import TextBlob
import pandas as pd


class Analizer():

    def score(self, text: str) -> float:
        return TextBlob(text).sentiment.polarity

    def predict(self, path: str):
        df = self.read_data(path)
        df['score'] = df['text'].apply(self.score)
        df['pred'] = pd.cut(df['score'], bins=5, labels=[1, 2, 3, 4, 5])
        return df
