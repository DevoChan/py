import random

print ("Guess the number o:")
print ('Type "exit" to leave')
random_number = random.randint(0,9)
game = ""
while game != "exit":
    game = input()
    if game == "exit": continue
    game = int(game)
    if game > random_number : print ("greater")
    if game < random_number : print("lower")
    if game == random_number : 
        print("Congrats you win, the number was: " + str(random_number))
        random_number = random.randint(0,9)
        print("Let's try to guess a new number :)")