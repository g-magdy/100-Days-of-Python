import pandas
student_dict = {
    "student" : ['george', 'harry', 'beth', 'john'],
    "socres" : [12, 23, 34, 11]
}
# print(student_dict)

# for (key, value) in student_dict.items():
#     print(value)
    

students = pandas.DataFrame(student_dict)
# print(students)

# for (key, value) in students.items():
#     print(value)

for (index, row) in students.iterrows():
    print(row, end='\n\n')
