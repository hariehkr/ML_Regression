import zipfile
import sys, os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) # Modify the path dynamically

from src.datascience.entity.config_entity import DataIngestionConfig
import urllib.request as request
from src.datascience import  logger




## component_Data Ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_URL,
                                                    filename=self.config.local_data_file)
            logger.info(f"Downloaded file {filename} file with following info:\n {headers}")
        else:
            logger.info(f"File  already exists")

    def extract_zip_file(self):
        """
        zip_file_path : str
        extracts the zip file into the data directory
        function returns None
        """
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)