from utils.query import Query
from collector.collectorConfig import CollectorConfig
from collector.tweetCollector import TweetCollector
from analizer.analizer import Analizer
from cleaner.cleaner import Cleaner


def main():
    config = CollectorConfig()
    collector = TweetCollector(config)
    cleaner = Cleaner(config)
    analizer = Analizer(config)

    query = Query(["Ecuador%20AND%20Tri"],
                  date_start="2021-09-06")
    collected_data = collector.collect(query)
    clean_data = cleaner.clean(collected_data)
    analized_data = analizer.analize(clean_data)
    print(analized_data)


if __name__ == "__main__":
    main()
