from math import factorial 
def croche(n):
    facteurs_premiers = [] #facteurs premiers
    for i in range(2,n):
        if n % i == 0:
            facteurs_premiers.append(i)

    mult_facteurs_premiers = [] #multiples des facteurs premiers
    for i in range(0,len(facteurs_premiers)):
        fact_prem = facteurs_premiers[i]
        for j in range(1,(n//fact_prem)):
            if fact_prem*j not in mult_facteurs_premiers:
                mult_facteurs_premiers.append(fact_prem*j)
        fact_prem = facteurs_premiers[i]
    mult_facteurs_premiers.append(n)
    
    denom = 1
    for i in range(len(mult_facteurs_premiers)):
        denom *= mult_facteurs_premiers[i]
    
    num = factorial(n)
    
    return num//denom

def prem_mult(m):
    n = 1
    while croche(n)%m!=0:
        n += 1
    return n