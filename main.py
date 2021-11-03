from art import logo,vs
from game_data import data
import random
from replit import clear
print(logo)
game_on=True
score=0
while game_on:
    a=random.randint(0,len(data))
    b=random.randint(0,len(data))
    print(f"compareA: {data[a]['name']},{data[a]['description']} from {data[a]['country']}")
    print(vs)
    print(f"compareB: {data[b]['name']},{data[b]['description']} from {data[b]['country']}")
    choice=input("who has more followers type 'A' or Type'B' ").lower()
    if choice=='a':
        if data[a]["follower_count"]>data[b]['follower_count']:
            score+=1
        else:
            game_on=False
    elif choice=='b':
        if data[b]["follower_count"]>data[a]['follower_count']:
            score+=1
        else:
            game_on=False
    clear()
    print(f"your score is {score}")
    



