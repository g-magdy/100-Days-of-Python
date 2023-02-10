# the module name is prettytable
# the class name is PrettyTable (in PascalCase)
from prettytable import PrettyTable

my_table = PrettyTable()

cities = ['Berlin', 'California', 'Giza', 'Aswan', 'Luxor']
names = ['Pikachu', 'Squirtle', 'Charmander']
types = ['Electric', 'Water', 'Fire']
my_table.add_column("Pokemon name", names)
my_table.add_column("Types", types)
# my_table.add_column("Cities", cities)
my_table.align = 'l'

# print(my_table)
second_term_courses = [
    'Advanced Logic Design', 
    'Data sturctures and algorithms',
    'Electronic circuits',
    'Numerical Analysis',
    'Electrodynamics',
    'Mechanical engineering',
    'Technical writing'
]
x = PrettyTable()
x.add_column("Courses", second_term_courses)
# x.add_row()
print(x)