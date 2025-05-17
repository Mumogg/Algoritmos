def numberN(n, lis = None):
    if lis is None:
        lis = []
    if n==0:
        return lis
    
    lis.append(n)
    return numberN(n-1, lis)  

print(numberN(8))



#def factTail(n,accumulator = 1):
#    if(n==0):
 #       return accumulator
    
  #  accumulator = accumulator * n

  #  return factTail(n-1,accumulator)