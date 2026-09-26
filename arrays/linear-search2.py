def linearSearch(arr, x):
    for i in range (len(arr)):
        if arr [i] == x:
            return i
    return -1
    
arr = [20, 40, 70, 10, 12, 11, 29, 75, 46]
x = 10

result = linearSearch(arr, x)
print("the element is at index:", result)