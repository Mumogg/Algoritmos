def linear_search(arr, target):
    size = len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    
    return -1

