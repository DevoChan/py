import math

def get_number():
    return int(input("Type a number"))

def prime (number):
    for i in range (2, int(math.sqrt(number)+1)):
        if number % i == 0   : return "Not prime number"
    return "Prime number"

print ("Determine if a number is prime or not")
number = get_number()
print(prime(number))