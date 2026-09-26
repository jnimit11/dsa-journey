def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1 
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
        arr[j+1] = key
    return arr
        

arr = [90, 80, 70, 60, 50, 40, 30, 20, 10]
result = insertionSort(arr)
print("insertion sort of the given array is:", result)