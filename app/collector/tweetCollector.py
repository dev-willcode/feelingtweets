from collector.collectorConfig import CollectorConfig
from twscrapper.scrapper import scrap
import os


class TweetCollector:

    def __init__(self, config: CollectorConfig):
        self.config = config

    def __generateOutputFilePath(self, file_number: int = 0):
        main_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.path.join(main_path, self.config.output_folder)

        filename = self.__generateFileName(file_number)
        extension = ".csv"
        output_path = os.path.join(dir_path, filename) + extension

        if(os.path.exists(output_path)):
            return self.__generateOutputFilePath(file_number + 1)

        return output_path

    def __generateFileName(self, file_number: int):
        name = 'tweets_collected_at_'
        name += self.config.date_start

        if(self.config.date_end):
            name += "_until_" + self.config.date_end

        if file_number > 0:
            name += "(" + file_number.__str__() + ")"
        return name

    def collect(self, query: list):
        print("start collecting " +
              "since: " + self.config.date_start +
              " until: " + self.config.date_end +
              " tweets for search: " + query.__str__())

        tweets = scrap(words=query,
                       since=self.config.date_start,
                       until=self.config.date_end,
                       lang=self.config.language,
                       interval=1,
                       display_type="Top", save_images=False,
                       resume=False, filter_replies=False, proximity=False)
        output = self.__generateOutputFilePath()
        print("saving data results in: " + output)
        tweets.to_csv(output)
        print("collect finished.")
        return tweets
