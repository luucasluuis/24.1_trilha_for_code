import math

n = 2

somatorio = 0

while n < 100000:
    somatorio += 1 / (n * math.log(n)**2)
    print(somatorio)
    n += 1
