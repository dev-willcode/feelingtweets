
from utils.query import Query
from utils.config import CollectorConfig
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

    search = "(ECUADOR OR TRI OR FEF) AND (FUTBOL OR FÚTBOL OR partido OR selección OR seleccion OR copa OR mundial)"
    query = Query(search, date_start="2021-09-06", limit_tweets=100)
    collected_data = collector.collect(query, True)
    cleaned_data = cleaner.clean(collected_data, True)
    translate_data = traductor.traduce(cleaned_data, True)
    if translate_data is not None:
        analized_data = analizer.analize(translate_data["traduced"])
        print(analized_data)
        analized_data = analizer.analize(translate_data["original"])
        print(analized_data)
