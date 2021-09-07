from collector.collectorConfig import CollectorConfig
from os import path
import os


class FileNamer:
    config: CollectorConfig

    def __init__(self, config: CollectorConfig):
        self.config = config

    def generateOutputFilePath(self, folder: str,
                               filename: str, extension: str,
                               file_number: int = 0):
        main_path = self.config.output_folder
        if(not path.exists(main_path)):
            # path por defecto, en el home directory.
            main_path = path.join(path.expanduser("~"), "Analysis")

        dir_path = path.join(main_path, folder)
        if(not path.exists(dir_path)):
            self.create_subfolder(dir_path)

        output_path = path.join(dir_path,
                                self.append_file_number
                                (filename, file_number)) + extension

        if(path.exists(output_path)):
            return self.generateOutputFilePath(folder, filename,
                                               extension, file_number+1)
        return output_path

    def create_subfolder(self, folder: str):
        os.makedirs(folder)

    def append_file_number(self, filename: str, number: int):
        if(number == 0):
            return filename
        return filename + "(" + number.__str__() + ")"
