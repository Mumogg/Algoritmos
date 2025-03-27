arr = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
def countNegatives(x, arr):
    size = len(arr)
    negative = 0
    for i in range(0,size):
        for j in range(len(arr[i])):
            if(arr[i][j]<0):
                negative+=1
        
    return negative


print(countNegatives(arr))