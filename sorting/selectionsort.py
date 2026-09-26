def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [50, 38, 75, 29, 11, 17, 20, 37]
result = selectionSort(arr)
print("selection sort of the given array is:", result)