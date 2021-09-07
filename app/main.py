from collector.collectorConfig import CollectorConfig
from collector.tweetCollector import TweetCollector
from cleaner.cleaner import Cleaner


def main():
    config = CollectorConfig(date_start='2021-09-06')
    collector = TweetCollector(config)
    cleaner = Cleaner(config)

    collected_data = collector.collect(["Ecuador%20AND%20Tri"])
    clean_data = cleaner.process(collected_data)


if __name__ == "__main__":
    main()
