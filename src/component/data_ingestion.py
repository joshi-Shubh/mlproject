import os
import sys
from src.exception import Custome_Exception
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataingestionConfig :
    train_data_path = os.path.join('artifacts',"train.csv")
    test_data_path = os.path.join('artifacts',"test.csv")
    raw_data_path = os.path.join('artifacts',"data.csv")

class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataingestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component ")     
        try:
            pass
        except:
            pass    