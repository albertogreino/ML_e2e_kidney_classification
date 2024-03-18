import os
import zipfile
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.source_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
