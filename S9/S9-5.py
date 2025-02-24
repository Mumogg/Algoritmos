n = int(input("Introduce un número: "))
def generate_inverted_triangle(n):
    lista = []
    v = n
    for i in range(n):
        lista.append("*" * v)
        v -= 1
        if n == 0:
            break
        
    return lista
print(generate_inverted_triangle(n))