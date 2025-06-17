def merge(l1,s,m,e):
    i = s
    j = m+1

    ans = []

    while(i<=m and j<=e):
        if(l1[i]<l1[j]):
            ans.append(l1[i])
            i+=1
        elif(l1[i]>l1[j]):
            ans.append(l1[j])
            j+=1
        elif(l1[i]==l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i+=1
            j+=1
    
    while(i<=m):
        ans.append(l1[i])
        i+=1

    while(j<=e):
        ans.append(l1[j])
        j+=1

def mergeSortHelper(l1,s,e):
    if s>=e:
        return
    
    m = s + (e-s)//2

    mergeSort(l1,s,m)
    mergeSort(l1,m+1,e)

    merge(l1)
    
    return



def mergeSort(l1):
    return mergeSortHelper(l1,0,len(l1)-1)

l1 = [8,15,3,1,4,9,11,2]
mergeSort(l1)