
from utils.query import Query
from collector.collectorConfig import CollectorConfig
from collector.tweetCollector import TweetCollector
from analizer.analizer import Analizer
from cleaner.cleaner import Cleaner
from traductor.traductor import Traductor


if __name__ == "__main__":
    config = CollectorConfig(input_collect_language="es")
    collector = TweetCollector(config)
    cleaner = Cleaner(config)
    traductor = Traductor(config)
    analizer = Analizer()

    # search = "(ECUADOR OR TRI) AND (FUTBOL OR FÚTBOL OR partido OR selección)"
    # query = Query(search, date_start="2021-09-06", limit_tweets=3200)
    # collected_data = collector.collect(query, True)
    collected_data = r"C:\Users\willy\Documents\Analisys\collected\tweets_collected_at_2021-09-06_until_2021-09-13.csv"
    cleaned_data = cleaner.clean_file(collected_data, True)
    translate_data = traductor.traduce(cleaned_data, True)
    if translate_data is not None:
        analized_data = analizer.analize(translate_data["traduced"])
        print(analized_data)
        analized_data = analizer.analize(translate_data["original"])
        print(analized_data)
