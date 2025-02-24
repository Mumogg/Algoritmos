n = int(input("Introduce un número: "))

def generate_floyds_triangle(n):
    lista = []
    cn = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(cn))
            cn += 1
        lista.append(' '.join(row))
    return lista

print(generate_floyds_triangle(n))
