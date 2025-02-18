n = int(input("Introduce un número: "))
def generate_triangle(n):
    lista = []
    v = n // 2
    for i in range(n):
        if lista == v:
          lista.append("*" * n)  
        else:
            lista.append(" " *n)
            
        v += 2
        
    return lista
print(generate_triangle(n))