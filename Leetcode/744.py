def nextGreatestLetter(arr, target):
        size = len(arr)
        for i in range(0,size):
             if i > target:
                return i
        
        return arr[0]