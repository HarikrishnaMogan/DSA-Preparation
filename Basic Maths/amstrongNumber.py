
n = 153

# if its is amstrong 
#1^3+5^3+3^3 = 153

def checkAmstrongNum(n):
    an =0
    x =n
    while n > 0:
        an = (n%10)**3+an
        n = n//10
    if an == x:
        return True
    else:
        return False


print(checkAmstrongNum(n))

        
        
