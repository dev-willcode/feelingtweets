
from utils.namer import FileNamer
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

    def __generateFileName(self):
        name = 'tweets_collected_at_'
        name += self.config.date_start

        if(self.config.date_end):
            name += "_until_" + self.config.date_end
        return name

    def collect(self, query: list):
        namer = FileNamer(self.config)
        print("Start collecting....")
        print("query = " + query.__str__() +
              " since: " + self.config.date_start +
              " until: " + self.config.date_end)

        tweets = scrap(words=query,
                       since=self.config.date_start,
                       until=self.config.date_end,
                       lang=self.config.language,
                       interval=1,
                       display_type="Top", save_images=False,
                       resume=False, filter_replies=False, proximity=False)

        output = namer.generateOutputFilePath(
            self.config.output_folder_collected,
            self.__generateFileName(), ".csv")
        print("saving collecting results...")
        tweets.to_csv(output)
        print("saved in: " + output)
        print("Collecting process finished.")
        return output
