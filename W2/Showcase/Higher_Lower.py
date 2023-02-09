#we have two items, compare the secomd to the first each time, regardless of the result the second is compared to the third and so on
from game_data import data
from Art_of_w2 import Higher_Lower, vs
import random
import os
A = random.choice(data)
B = random.choice(data)
while B["name"] == A["name"]:
    B = random.choice(data)
##################
def judge(answer):
    '''takes the answer and returns its validity (true or false) by comparing the followers of the two global objects and the answer'''
    if A["follower_count"] > B["follower_count"]:
        return answer.lower() == 'a'
    elif B["follower_count"] > A["follower_count"]:
        return answer.lower() == 'b'
    return False # if the answer is neither a nor b
####################
final_score = 0
while True:
    os.system("cls")
    print(Higher_Lower)
    if final_score > 0:
        print(f"You are right! current score is {final_score}")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Againist B: {B['name']}, a {B['description']}, from {B['country']}")
    answer = input("Who has more followers ? Type 'A' or 'B' : ").lower()
    if judge(answer) : 
        final_score += 1
        A = B
        B = random.choice(data)
        while B["name"] == A["name"]:
            B = random.choice(data)            
    else:
        break
print(f"Game over: your score is {final_score}")