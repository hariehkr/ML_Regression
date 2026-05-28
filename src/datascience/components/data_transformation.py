import sys, os
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

sys.path.append(str(Path(__file__).resolve().parents[1])) # Modify the path dynamically

from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience import  logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data =pd.read_csv(self.config.data_path)

        # split the data into train and test 75/ 25 ration
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("splitteddata into train and test set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        



