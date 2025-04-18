import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")
        try:
            # Read the dataset
            df=pd.read_csv('notebook/data/stud.csv')    
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            # Save the raw data
            df.to_csv(self.config.raw_data_path, index=False, header=True)
            logging.info('Train test split initiated')
            # Split the data into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  
            # Save the train and test sets  
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            logging.info('Ingestion of the data is completed')
            return (
                self.config.train_data_path,
                self.config.test_data_path,
                self.config.raw_data_path
            )

        except  Exception as e:
            raise CustomException(e, sys)
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
        