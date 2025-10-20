import random
lst = [27, 11, 23, 38]
a = random.choice(lst)
x = int(input("Enter your guess"))
if x == a:
    print("Your guess is accurate")
elif x < a:
    print("Your guess is less than the answer")
else:
    print("Your guess is greater than answer")