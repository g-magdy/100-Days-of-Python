'''
This program simulates the action of flipping a coin a lot of times
Let's explore the probability that n heads occur successively
input: n
output: number of flips it took to filp n heads in a row (including the head flips themselves)
'''
import random
print("Hello, Let's flip some coins")
target_n = int(input("enter the number of heads you'd like to reach in a row: "))
flips_counter = 0
streak = 0
while (streak < target_n):
    flip = random.randint(0, 1)
    flips_counter += 1
    if (flip == 1):
        streak += 1
    else:
        streak = 0
print(f"Congratulations, we have flipped {target_n} heads in a row after {flips_counter} total flips")