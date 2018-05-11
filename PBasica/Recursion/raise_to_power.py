import sys
sys.setrecursionlimit(2002)

def power_fnc (base,power):
    if power == 1 : return base
    return base * power_fnc(base, power - 1)

base = int(input("Write the base: "))
power = int(input("Write the power: "))
print(power_fnc(base, power))