print("welcome back to Python!")
s = input("What is your name ? ")
print(f"Hello {s} 😇")
# comments start with hashes
'''
Multi-line comments have brighter color
'''
a = "This is a \"Strange\" thing"
b = 123
print(a)
# python is dynamically typed

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=' ')
    if i == 9:
        print()
    
scores = [12, 45, 23, 11]
for score in scores:
    print(score + 1, end=' ')
print()
for i in range(1, 10, 2):
    print(i, end=' ')