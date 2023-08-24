import requests
from dotenv import dotenv_values
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_url = dotenv_values(dotenv_path=".env")["SHEET"]
        self.response = requests.get(self.sheet_url) # type: ignore
        self.response.raise_for_status()
        self.sheet_data : dict = self.response.json()
        self.prices : list = self.sheet_data["prices"]
                
    def get_prices(self):
        return self.prices
    
    def edit_row(self, data : dict, row_id : int):
        url = f"{self.sheet_url}/{row_id}"
        response = requests.put(url=url, json=data)
        response.raise_for_status()