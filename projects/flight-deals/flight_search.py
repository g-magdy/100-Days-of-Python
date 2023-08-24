import requests
from dotenv import dotenv_values
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = dotenv_values(dotenv_path=".env")["TEQUILA_API_KEY"]

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def getIATAcode(self, city_name : str) -> str:
        url = f"{TEQUILA_ENDPOINT}/locations/query"
        head = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "term": city_name
        }
        response = requests.get(url=url,
                                     headers=head, # type: ignore
                                     params=params)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
    
    
    def search_flights(self,
                        origin_city_code,
                        destination_city_code,
                        from_time,
                        to_time
                        ):
        
        url = "https://api.tequila.kiwi.com/v2/search"
        head = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from" : 5,
            "nights_in_dst_to" : 10,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        response = requests.get(url=url,
                                     headers=head, # type: ignore
                                     params=params)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flightData = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["utc_departure"],
            return_date=data["route"][1]["utc_departure"]
            )
        print(f"{flightData.destination_city} : {flightData.price} EURO")
        return flightData
