first_dic = {
    "code" : "Machine instructions",
    "binary" : "Number system assosciated with machines",
    "FF" : "255 in hexadacimal",
}
# retrieving information
#print(first_dic["binary"])

france_capitals = {
    "Paris",
    "Lille",
    "Dijon",
}

germany_capitals = {
    "Berlin",
    "Hamburg",
    "Stutt"
}

travel_log = {
    "France" : { # nested dictionary
        "cities_visited" : ["berlin", "hamburg", "bayern"], # the value is a list
        "numberOFvisits" : 12,
        },
    "Germany" : { # nested dictionay
        "Capitals" : germany_capitals, # the value is a list
        },
}
print(travel_log)