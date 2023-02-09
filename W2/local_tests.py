# def func(a):
#     a.append(90)
# a = [1, 12] 
# func(a)
# print(a)

# deck = [11, 3]

# deck[deck.index(11)] = 1
# print(deck) b

a = 10

def f():
    a = 20
    print(a)

#f()

# In python there is no block  scope : no scope for if or while or for 
# the scope of the stuff inside s the same scope of the enclosing function definition or global
a = 10

if a > 5:
    b = 123
elif a > 15:
    b = 90
else:
    b = 1
    
# print(b)

data = [
    {
        'name' : 'george',
        'follower_count' : 123,
        'description' : 'Student',
        'country' : 'Egypt'
    },
    {
        'name' : 'messi',
        'follower_count' : 993,
        'description' : 'player',
        'country' : 'argentina'
    },
    {
        'name' : 'abdeen',
        'follower_count' : 100,
        'description' : 'prof',
        'country' : 'Egypt'
    },
]
CompDict = {
    'name' : 'apple',
    'follower_count' : 9999,
    'description' : 'tech',
    'country' : 'US'
}

print(CompDict['country'])


if CompDict:
    print("This is true!!!")