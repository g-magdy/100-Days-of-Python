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

f()

# In python there is no block  scope : no scope for if or while or for 
# the scope of the stuff inside s the same scope of the enclosing function definition or global
a = 10

if a > 5:
    b = 123
elif a > 15:
    b = 90
else:
    b = 1
    
print(b)