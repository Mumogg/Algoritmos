def fibonicci(n):

    if(n==0):
        return 1
    if(n==1):
        return 1

    return fibonicci(n-1) + fibonicci(n-2)

print(fibonicci(5)) 