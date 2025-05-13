def sum(n):
    if(n==1): #Paso 1
        return 1 
    
    smallAns = sum(n-1) #Paso 2

    ans = n + smallAns #Paso 3
    return ans


print(sum(500))