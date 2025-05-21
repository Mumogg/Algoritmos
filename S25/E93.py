# def find_first_index(arr, element):
#     if (len(arr) == 0):
#         return -1
#     if (arr[0]==element):
#         return 0 
    
#     ans = find_first_index(arr[1:], element)

#     if ans == -1:
#         return ans
#     else:
#         return ans +1
    
# print(find_first_index([3,2,5,2,8,2,1],2))
# print(find_first_index([3,2,5,2,8,2,1],5))
# print(find_first_index([3,2,5,2,8,2,1],8))

def last_index(arr, x, idx= 0):
    if (len(arr) == 0):
        return -1
    
    ans = last_index(arr[1:],x,idx+1)

    if ans != -1:
        return ans
    if arr[0] == x:
        return idx
    return -1
    
print(last_index([3,2,5,2,8,2,1],5))