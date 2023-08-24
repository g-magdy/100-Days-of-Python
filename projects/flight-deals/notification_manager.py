from dotenv import dotenv_values
from twilio.rest import Client
TWILIO_SID = dotenv_values(dotenv_path=".env")["TWILIO_SID"]
TWILIO_AUTH_TOKEN = dotenv_values(dotenv_path=".env")["TWILIO_AUTH_TOKEN"]
TO = dotenv_values(dotenv_path=".env")["TO"]
FROM = dotenv_values(dotenv_path=".env")["FROM"]
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, data):
        day_start = data.out_date.split("T")[0]
        time_start = f"{data.out_date.split('T')[1][:5]} UTC"
        day_end = data.return_date.split("T")[0]
        time_end = f"{data.return_date.split('T')[1][:5]} UTC"
        msg = (
            "LOW PRICE ALERT\n"
            f"only {data.price} EURO\n"
            f"to fly from {data.origin_city}-{data.origin_airport} "
            f"to {data.destination_city}-{data.destination_airport}\n"
            f"from {day_start} at {time_start} to \n{day_end} at {time_end}."
        )
        print(msg)
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            to=TO,  # type: ignore
            from_=FROM,
            body=msg
        )