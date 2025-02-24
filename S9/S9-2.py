#Hollow Square of side N
#Problem Description:
#You are given an integer n. 
#Your task is to return a hollow square pattern of size n x n made up of the character '*', 
#represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle 
#except for side lengths of 1 and 2).


##Input Parameters:
#n (int): The size of the square (number of rows and columns).

#Output:
#A list of strings where each string is a row of n characters, representing a hollow square.

#Example:
#Input: 3
#Output: ['***', '* *', '***']
 
#Input: 5
#Output: ['*****', '*   *', '*   *', '*   *', '*****']"

n = int(input("Introduce un número: "))
def generate_hollow_square(n):
    lista = []
    if n <= 0:
        return []
    elif n == 1:
        return ['*']
    elif n == 2:
        return ['**', '**']
    
    lista.append('*'*n)
    for i in range(n-2):
        lista.append('*' + ' '*(n-2) + '*')

    lista.append("*" * n)
    return lista

print(generate_hollow_square(n))