def count_digits(n):
    if(n >= 1 and n<=9):
        return 1
    elif(n==0):
        return 1
    
    smallNum = int(n/10)
    smallAns = count_digits(smallNum) #Paso 2

    ans = 1 + smallAns #Paso 3
    return ans

print(count_digits(565648))