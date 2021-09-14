
class CollectorConfig:
    output_folder: str
    output_folder_collected: str
    output_folder_cleaned: str
    output_folder_analized: str
    output_folder_traduced: str
    collector_column: str
    cleaner_column: str
    analizer_column: str
    input_collect_language: str
    output_traduce_language: str

    def __init__(self,
                 output_folder="C:\\Users\\willy\\Documents\\tweetfeels",
                 output_folder_collected="collected",
                 output_folder_cleaned="cleaned",
                 output_folder_analized="analized",
                 output_folder_traduced="traduced",
                 collector_column="tweet",
                 cleaner_column="clean_tweet",
                 analizer_column="analized_tweet",
                 input_collect_language="auto",
                 output_traduce_language="en",
                 ):
        self.output_folder = output_folder
        self.output_folder_collected = output_folder_collected
        self.output_folder_cleaned = output_folder_cleaned
        self.output_folder_analized = output_folder_analized
        self.output_folder_traduced = output_folder_traduced
        self.collector_column = collector_column
        self.cleaner_column = cleaner_column
        self.analizer_column = analizer_column
        self.input_collect_language = input_collect_language
        self.output_traduce_language = output_traduce_language
