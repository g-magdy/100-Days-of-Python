#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
        
TOMORROW = datetime.now() + timedelta(days=1)
AFTER_6MONTHS = TOMORROW + timedelta(days=6*30)

flightSearch = FlightSearch()
dataManager = DataManager()
messenger = NotificationManager()

sheet_data = dataManager.get_prices()
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flightSearch.getIATAcode(row["city"])
        new_row : dict[str, dict] = {"price" : row}
        dataManager.edit_row(data=new_row, row_id=row["id"])
    else:
        data = flightSearch.search_flights(
            origin_city_code="LON",
            destination_city_code=row["iataCode"],
            from_time=TOMORROW.strftime("%d/%m/%Y"),
            to_time=AFTER_6MONTHS.strftime("%d/%m/%Y")
        )
        current_price = float(data.price) #type: ignore
        if current_price < float(row["lowestPrice"]):
            messenger.send_message(data)
