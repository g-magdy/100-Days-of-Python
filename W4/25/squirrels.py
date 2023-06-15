import pandas

'''
figure out how many squirrels in each color
'''
    
data = pandas.read_csv("2018-dataset.csv")

fur_colors = data["Primary Fur Color"].to_list()
cg = fur_colors.count("Gray")
cr = fur_colors.count("Cinnamon")
cb = fur_colors.count("Black")
mydict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [cg, cr, cb]
}

dataframe = pandas.DataFrame(mydict)

dataframe.to_csv("numSquirrels.csv")