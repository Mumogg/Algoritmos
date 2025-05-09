def factorial(n):
    if(n<=1 ):
        return 1 
    mul = factorial(n-1)
    a = n*mul
    return a 