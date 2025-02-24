n = int(input("Introduce un número: "))

def generate_triangle(n):
    lista = []
    for i in range(1, n):
        row = str(i) 
        lista.append(row)
    return lista

print(generate_triangle(n))

