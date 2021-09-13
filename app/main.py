
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
    # traductor = Traductor(config)

    query = Query("Ecuador AND Gonzalo Plata OR Tri OR Tricolor",
                  date_start="2021-09-06",
                  limit_tweets=40)
    collected_data = collector.collect(query, True)
    cleaned_data = cleaner.clean(collected_data, True)
    # translate_data = traductor.traduce(cleaned_data)
    # print(translate_data)
    analized_data = analizer.analize(cleaned_data, True)
    print(analized_data)


if __name__ == "__main__":
    main()
