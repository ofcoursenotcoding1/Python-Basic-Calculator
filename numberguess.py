import random
a = input("Enter your name to play the game: ")
b = int(input("Enter the lower limit of the number: "))
c = int(input("Enter the upper limit of the number: "))
rand = random.randint(b, c)

while True:
    guess = input(f"Enter the number between {b} and {c}: ")
    if guess > rand:
        print("To high")
    elif guess < rand: 
        print("To low")
    elif guess == rand:
        print("You got it!")
        break






