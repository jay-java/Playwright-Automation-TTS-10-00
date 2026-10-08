import random
from enum import Flag

print(random.randint(100000 ,999999))

list = [1,2,3,4,456.456,45764357,False,"python",4567.65]
print(list)
print(random.choice(list))

num = random.randint(1 ,20)

while True:
    guess = int(input('enter your guess:'))
    if guess == num:
        print("number matched")
        break
    elif guess > num:
        print("higher numer")
    elif guess < num:
        print("lower numer")