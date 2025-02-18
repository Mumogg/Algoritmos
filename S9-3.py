n = int(input("Introduce un número: "))
m = int(input("Introduce un número: "))
def generate_square(n,m):
    lista = []
    for i in range(n):
        lista.append("*" * m)

        
    return lista


print(generate_square(n,m))