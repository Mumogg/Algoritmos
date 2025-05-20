def recursive_sum(li, accumulator=0):
    if (len(li) == 0):
        return accumulator
    return recursive_sum(li[1:], accumulator+ li[0])
   

l1 = [1, 2, 3, 4, 5,234]
print(recursive_sum(l1))

#def factTail(n,accumulator = 1):
#    if(n==0):
 #       return accumulator
    
  #  accumulator = accumulator * n
 
  #  return factTail(n-1,accumulator)