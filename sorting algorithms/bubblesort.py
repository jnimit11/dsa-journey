def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [70, 20, 50, 30, 90, 5, 15]
result = bubbleSort(arr)
print("Array after applying bubble Sort:", result)