import pandas as pd
from fastapi import UploadFile

class DataAccess():
    def __init__(self):
        self._data = None # access by get data only
   
    # getter
    def get_data(self):
        return self._data
    
    def data_from_csv(self, csv_file: UploadFile):
        self._data = pd.read_csv(csv_file.file) # need to check file.csv with raise
        return self._data
        
    def delete_data(self):
        self._data = None