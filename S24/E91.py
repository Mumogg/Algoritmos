def numberN(n, accumulator = 0):
    if n==0:
        return accumulator 
    
    accumulator = accumulator + 1
    print(n)

    return numberN(n-1, accumulator)

numberN(6)



#def factTail(n,accumulator = 1):
#    if(n==0):
 #       return accumulator
    
  #  accumulator = accumulator * n

  #  return factTail(n-1,accumulator)