import datetime as dt
from collector.collectorConfig import CollectorConfig
from collector.tweetCollector import TweetCollector
from cleaner.cleaner import Cleaner


def main():
    config = CollectorConfig(date_start="2021-09-01")
    collector = TweetCollector(config)
    cleaner = Cleaner()

    data = collector.collect(["Ecuador", "tri"])
    cleaner.clean(data)


if __name__ == "__main__":
    main()
