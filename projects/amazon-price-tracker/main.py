import dotenv, smtplib, requests, bs4, lxml
config : dict = dotenv.dotenv_values()
item_url = "https://www.amazon.eg/-/en/gp/product/B0BXNW1KFB/ref=ox_sc_act_title_1?smid=A1PIQIIOGD2ESG&th=1"
my_header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.6"
}

response = requests.get(url=item_url, headers=my_header)
response.raise_for_status()
soup = bs4.BeautifulSoup(markup=response.text, features="lxml")
price_element = soup.select_one("span.a-price-whole")
name_element = soup.select_one("h1 span#productTitle ")
name = name_element.text.strip() #type: ignore
price = price_element.text.strip('.') #type: ignore
price = int(price.replace(',', ''))

if price < 12000:
    notification = f"Subject: YOUR WANTED OFFER \n{name}\n{price}EGP"
    try : 
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=config["FROM_ADDRESS"], password=config["APP_PASSWORD"])
            connection.sendmail(
                from_addr=config["FROM_ADDRESS"],
                to_addrs=config["TO_ADDRESS"],
                msg=notification
            )
            print("Mail was sent sucessfully")
    except smtplib.SMTPException as e:
        print(e)