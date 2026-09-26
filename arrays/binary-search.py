# def binarySearch(arr, x, i, j):
#     while i <= j:
#         mid = i + (j - i) // 2
#         if arr[mid] == x:
#             return mid
        
#         elif arr[mid] < x:
#             return binarySearch(arr, x, mid + 1, j)
#         else:
#             return binarySearch(arr, x, i, mid - 1)
#     return -1

# arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
# x = 5
# i = 0
# j = len(arr) -1

# result = binarySearch(arr, x, i, j)
# print(" the element you searched is present at index:", result)

#this is recurive approach
def binarySearch(arr, x, i , j):
    while i <= j:
        mid = i + (j-i) // 2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            return binarySearch(arr, x, mid+1, j)
        
        else:
            return binarySearch(arr, x, i, mid-1)
    return -1

arr = [20, 30, 40, 50, 60, 70, 80, 90, 95, 99, 100]
x = 90
i = 0
j = len(arr) -1

result = binarySearch(arr, x, i, j)
print("The element searched is at index:", result) 