n = int(input("Introduce un número: "))

def generate_triangle(n):
    lista = []
    v = n
    for i in range(n):
        a = '*' * (2 * v-1)
        spaces = ' ' * (n - v)
        lista.append(spaces + a + spaces)
        v-=1
    return lista

# Generar el triángulo
print(generate_triangle(n))   

