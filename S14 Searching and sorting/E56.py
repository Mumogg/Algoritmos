def selection_sort(lst):
    n = len(lst)
    for passes in range(n):
        min_index = passes
        for i in range(passes + 1, n):
            if lst[i] < lst[min_index]:
                min_index = i
        # Intercambiar el elemento mínimo encontrado con el primer elemento de la pasada
        lst[passes], lst[min_index] = lst[min_index], lst[passes]
        print(lst)
    return lst

lst = [120, 25, 11, 34, 90, 22]
print("Lista ordenada:", selection_sort(lst))