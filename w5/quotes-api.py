import json, requests, termcolor
categories = ['age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success']
choice = input(termcolor.colored("Welcome to quotify :) show all categories ? ", color="yellow"))
if choice == 'y' or choice.lower() == 'yes':
    for category in categories:
        print(category, end=", ")

category = input(termcolor.colored("choose a category (type 'a' for any): ", color="yellow"))
if category == 'a':
    url = "https://api.api-ninjas.com/v1/quotes"
else:
    url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
headers = {
    'X-Api-Key': "uQA46rsQGuzaVAW7pYnw2Q==uuv2Yqwmj0xBkZXk"
}
response = requests.get(url=url, headers=headers)
response.raise_for_status()
data = response.json()
termcolor.cprint(data[0]["quote"], color="blue")
termcolor.cprint(data[0]["author"], color="yellow")
termcolor.cprint(data[0]["category"], color="cyan")