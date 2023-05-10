'''file = open("my_file.txt")
content = file.read()
print(content)
file.close() # to free up the resources'''
# better way :
with open("newFile.txt", mode="w") as file:
    file.write("this was created using Python")