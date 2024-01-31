

def fak_iter(x):
    fakultet = 1
    for i in range(1, x+1):
        fakultet *= i
    return fakultet

def fak_rek(x):
    if x > 1:
        return x * fak_rek(x-1)
    return 1
    
    
    #return x * fak_rek(x-1) if x > 0 else 1

print(fak_rek(5))