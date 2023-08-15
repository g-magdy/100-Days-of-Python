import smtplib
import datetime as dt
from random import randint

tom_email = "tom864849@gmail.com"
tom_pwd = "A3&)o%6D&#20S9O&qq"
jerry_email = "jerryj658@​yahoo.com"
jerry_pwd = "AP#6Zld$)f7#a%j5l"
app_pwd = "ethzzksfxndisaqq"
message = "hello"

now = dt.datetime.now()
if now.day == 13:
    # connect to email server 
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        n_quotes = len(quotes) - 1
        
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # start encrypted connection
        connection.starttls()
        # log in
        connection.login(user=tom_email, password=app_pwd)
        message = quotes[randint(0, n_quotes)]
        connection.sendmail(from_addr=tom_email,
                            to_addrs=jerry_email,
                            msg=f"Subject:Monday motivation\n\n{message}"
        )
