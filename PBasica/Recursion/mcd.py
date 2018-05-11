def mcd (a, b):
    if b == 0: return a
    return mcd(b, a % b)
num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
print (mcd(num1, num2))