import random

def search(arr, N, x): 
    for i in range(0, N): 
        if (arr[i] == x): 
            return i+1 
    return -1

def shellSort(arr, n): 
    gap=n//2
    while gap>0: 
        j=gap 
        # Check the array in from left to right 
        # Till the last possible index of j 
        while j<n: 
            i=j-gap # This will keep help in maintain gap value 
            while i>=0: 
                # If value on right side is already greater than left side value 
                # We don't do swap else we swap 
                if arr[i+gap]>arr[i]: 
                    break
                else: 
                    arr[i+gap],arr[i]=arr[i],arr[i+gap] 
                i=i-gap # To check left side also 
                            # If the element present is greater than current element  
            j+=1
        gap=gap//2

def rand(n, r):
    arr = []
    for i in range(n):
        arr.append(random.randrange(r))
    return arr