n = int(input("Introduce un número: "))

def generate_triangle(n):
    lista = []
    for i in range(n):
        a = 0+1 * (2 * i + 1)
        spaces = ' ' * (n - i - 1)
        lista.append(a + spaces + a)
    return lista

# Generar el triángulo
triangle = generate_triangle(n)

# Imprimir cada fila del triángulo
for row in triangle:
    print(row)