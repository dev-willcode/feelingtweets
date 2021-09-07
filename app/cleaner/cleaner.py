from collector.collectorConfig import CollectorConfig
from utils.namer import FileNamer
from pandas.core import series
import pandas as pd
import re as regex


class Cleaner:
    __config: CollectorConfig

    def __init__(self, config: CollectorConfig):
        self.__config = config

    def cleanFile(self, path: str):
        print("Start cleaning....")
        namer = FileNamer(self.__config)
        clean_data = self.__clean(path)
        df = pd.DataFrame()
        df['Text'] = clean_data
        output = namer.generateOutputFilePath(
            self.__config.output_folder_cleaned,
            self.__generateFileName(path), ".csv")
        print("saving cleaning results...")
        df.to_csv(output)
        print("saved in: " + output)
        print("Clean process finished.")
        return output

    def __generateFileName(self, path: str):
        filename_with_extension = path.split("\\")[-1]
        filename_without_extension = filename_with_extension.split(".")[0]

        name = 'cleaned_' + filename_without_extension
        return name

    def __clean(self, path: str):
        data = pd.read_csv(path)
        tweets_text = data["Text"]
        return self.__filtered(tweets_text)

    def __filtered(self, data: series.Series):
        listado = []
        INDICE_TEXTO = 1
        for tweet in data.to_dict().items():
            processed = tweet[INDICE_TEXTO]
            processed = self.__convertir_minusculas(processed)
            processed = self.__limpiar_menciones(processed)
            processed = self.__limpiar_links(processed)
            processed = self.__limpiar_caracteres_especiales(processed)
            processed = self.__limpiar_caracter_individual(processed)
            processed = self.__limpiar_caracter_individual_inicio(processed)
            processed = self.__limpiar_prefijo_b(processed)
            processed = self.__limpiar_hashtag(processed)
            processed = self.__limpiar_numeros(processed)
            processed = self.__limpiar_varios_espacios(processed)
            listado.append(processed)
        return listado

    def __convertir_minusculas(self, text: str):
        return text.lower()

    def __limpiar_links(self, text: str):
        regex_links = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        return regex.sub(regex_links, " ", text)

    def __limpiar_menciones(self, text: str):
        regex_menciones = "@[\w\-]+"
        return regex.sub(regex_menciones, " ", text)

    def __limpiar_hashtag(self, text: str):
        regex_hashtag = "#[\w\-]+"
        return regex.sub(regex_hashtag, " ", text)

    def __limpiar_caracteres_especiales(self, text: str):
        regex_caracteres_especiales = r"\W"
        return regex.sub(regex_caracteres_especiales, " ", text)

    def __limpiar_caracter_individual(self, text: str):
        regex_caracter_individual = r"\s+[a-zA-Z]\s+"
        return regex.sub(regex_caracter_individual, " ", text)

    def __limpiar_caracter_individual_inicio(self, text: str):
        regex_caracter_individual_inicio = r"\^[a-zA-Z]\s+"
        return regex.sub(regex_caracter_individual_inicio, " ", text)

    def __limpiar_varios_espacios(self, text: str):
        regex_varios_espacios = r"\s+"
        return regex.sub(regex_varios_espacios, " ", text)

    def __limpiar_prefijo_b(self, text: str):
        regex_prefijo_b = r"^b\s+"
        return regex.sub(regex_prefijo_b, " ", text)

    def __limpiar_numeros(self, text: str):
        regex_numeros = "[0-9]+"
        return regex.sub(regex_numeros, " ", text)
