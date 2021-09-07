from utils.query import Query
from collector.collectorConfig import CollectorConfig
from collector.tweetCollector import TweetCollector
from cleaner.cleaner import Cleaner


def main():
    config = CollectorConfig()
    collector = TweetCollector(config)
    cleaner = Cleaner(config)

    print("config: ", config.output_folder_collected)

    query = Query(["Ecuador%20AND%20Tri"])

    collected_data = collector.collect(query)
    clean_data = cleaner.cleanFile(collected_data)


if __name__ == "__main__":
    main()
