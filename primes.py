def isprime(p):
    if p == 1:
        return False
    for i in range(2,p):
        if (p%i)==0:
            return False
    return True
    pass