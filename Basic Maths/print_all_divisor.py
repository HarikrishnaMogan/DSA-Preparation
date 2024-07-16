# print all divisors
import math

def printAllDivisor(n):
    div = []
    k = int(math.sqrt(n))
    for i in range(1,k+1):
        if n%i == 0:
            div.append(i)
            if n//i != i:
                div.append(n//i)
    return div
        

print(printAllDivisor(6))
