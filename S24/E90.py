
def count_to_n(n, lis = None):
    if lis is None:
        lis = []
    if(n==0):
        return lis
    
    count_to_n(n-1, lis)
    
    lis.append(n)

    return lis

print(count_to_n(8))



#def factHead(n):
 #   if(n==0):
   #     return 1
  #  smallAnswer = factHead(n-1)

  #  finalAnswer = n * smallAnswer

 #   return finalAnswer