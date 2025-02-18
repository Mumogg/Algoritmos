n = int(input("Introduce un número: "))

def generate_square(n):
    list = []
    for i in range(n):
        list.append("*" * n)
    return list


print(generate_square(n))