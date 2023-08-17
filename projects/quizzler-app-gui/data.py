import requests, termcolor

categories = ['Any category',
     'General Knowledge',
     'Entertainment: Books',
     'Entertainment: Films',
     'Entertainment: Music',
     'Entertainment: Musicals & Theaters',
     'Entertainment: Television',
     'Entertainment: Video Games',
     'Entertainment: Board Games',
     'Science & Nature',
     'Science: Computers',
     'Science: Mathematics',
     'Mythology',
     'Sports',
     'Geography',
     'History',
     'Politics',
     'Arts',
     'Celebrities',
     'Animals',
     'Vehicles',
     'Entertainment: Comics',
     'Science: Gadgets',
     'Entertainment: Japanese Anime & Manga',
     'Entertainment: Cartoon & Animations']
def get_data() -> dict:
    termcolor.cprint("Welcome to the quiz game!", color="green")
    for i, ctg in enumerate(categories):
        termcolor.cprint(f"{i} : {ctg}", color="cyan")
        
    cat = int(input(termcolor.colored(f"Please choose your corresponding category number! ", color="yellow")))
    parameters = {
        "amount":10,
        "type":"boolean",
        "category": cat + 8
    }

    if cat == 0 or cat not in range(len(categories)):
        parameters.pop("category")

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]
