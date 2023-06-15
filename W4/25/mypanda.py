import pandas

mydict = {
    "Students" : ["George", "Mark", "Fathy", "Robert"],
    "Scores" : [12, 24, 13, 16]
}

df = pandas.DataFrame(mydict)
print(df)

df.to_csv("amazing.csv")