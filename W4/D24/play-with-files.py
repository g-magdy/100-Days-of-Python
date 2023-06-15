'''
Recall how to deal with files in Python
150723

"E:/GeoDocs/Written-with-Python.txt"
is equivalent to 
'''

PATH = "../E:/Write-with-Python.txt"
with open(PATH, mode='w') as myfile:
    myfile.write("Hello George")
