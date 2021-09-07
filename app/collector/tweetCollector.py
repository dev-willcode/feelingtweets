
from utils.query import Query
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

    def __generateFileName(self, query: Query):
        name = 'tweets_collected_at_'
        name += query.date_start

        if(query.date_end):
            name += "_until_" + query.date_end
        return name

    def collect(self, query: Query):
        namer = FileNamer(self.config)
        print("Start collecting....")
        print("query = " + query.search.__str__() +
              " since: " + query.date_start +
              " until: " + query.date_end)

        tweets = scrap(words=query.search,
                       since=query.date_start,
                       until=query.date_end,
                       lang=query.language,
                       interval=query.interval_day)

        output = namer.generateOutputFilePath(
            self.config.output_folder_collected,
            self.__generateFileName(query), ".csv")
        print("saving collecting results...")
        tweets.to_csv(output)
        print("saved in: " + output)
        print("Collecting process finished.")
        return output
