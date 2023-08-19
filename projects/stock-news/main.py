import os, requests, json, datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = datetime.datetime.today().date()
YESTERDAY = TODAY - datetime.timedelta(days=1)
DAY_BEFORE = YESTERDAY - datetime.timedelta(days=1)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = "https://www.alphavantage.co/query"
params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":os.environ.get("API_KEY")
}
request = requests.get(url=url, params=params)
request.raise_for_status()
time_series = request.json()["Time Series (Daily)"]
yesterday_stock = time_series[str(YESTERDAY)]
daybefore_stock = time_series[str(DAY_BEFORE)]
yesterday_close = float(yesterday_stock["4. close"])
daybefore_close = float(daybefore_stock["4. close"])
delta = yesterday_close - daybefore_close
percent = round(delta / yesterday_close, 2)*100
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
# articles[0]["title"]
url = (
    "https://newsapi.org/v2/everything?"
    f'q={COMPANY_NAME}&'
    f'from={YESTERDAY}&'
    'sortBy=popularity&'
    f'apiKey={os.environ.get("NEWS_API_KEY")}'
)
response = requests.get(url=url)
response.raise_for_status()
articles = response.json()["articles"]
msg = f"\n{COMPANY_NAME} {'🔺' if delta > 0 else '🔻'} {abs(percent)}%\n"
for article in articles[:3]:
    msg += f"Headline : *{article['title']}*\nBrief: {article['description']}\n"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
client = Client(os.environ.get("ACC_SID"), os.environ.get("AUTH_TOKEN"))
message = client.messages.create(
    to=os.environ.get("RECEIVER"),
    from_=os.environ.get("SENDER"),
    body=msg
)
print(message.status)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

