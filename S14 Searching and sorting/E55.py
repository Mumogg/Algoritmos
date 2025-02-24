def bubble_sort(lst):
    n = len(lst)
    for passes in range(0, n):
        for i in range(0,n-1-passes):
            if(lst[i]>lst[i+1]):
                lst[i],lst[i+1] =lst[i+1],lst[i]
    return lst


unsorted_list = [120,25,11,34,90,22]
sorted_list = bubble_sort(unsorted_list)
print("Sorted Elements :", sorted_list)