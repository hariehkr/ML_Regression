import os,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) # Modify the path dynamically
#os.chdir("../")
import pandas as pd
data=pd.read_csv("./artifacts/data_ingestion/winequality-red.csv")

from dataclasses import dataclass
from pathlib import Path
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience import logger


@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema)

        return data_validation_config
    
    
class DataValidation:
    def __index__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as status_file:
                        status_file.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as status_file:
                        status_file.write(f"Validation status: {validation_status}")
            return validation_status

        except Exception as e:
            raise e
try:
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.validate_all_columns()

except Exception as e:
    raise e