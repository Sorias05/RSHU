from algorithms import search, shellSort, rand

# Search
arr = rand(10, 20)
print("Array: ",arr) 
x = int(input("Enter digit you want to search: "))

result = search(arr, len(arr), x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result)     

# Sort
arr = rand(10, 20)
print("Input array: ",arr) 
  
shellSort(arr,len(arr)) 
print("Sorted array: ",arr) 