n = int(input("Introduce un número: "))
def generate_triangle(n):
    lista = []
    v = 1
    for i in range(n):
        lista.append("*" * v)
        if n == v:
            break
        elif n > v:
            v += 1
    return lista
print(generate_triangle(n))