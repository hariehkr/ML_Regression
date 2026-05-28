
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, 
                 params_filepath= PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

