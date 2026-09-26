def findminAndmax(arr, i, j):
    if i == j:
        min = arr(i)
        max = arr(j)
        
    elif i == j-1:
        if arr(i) < arr(j):
            min = arr(i)
            max = arr(j)
        else:
            min = arr(j)
            max = arr(i)
            
    else:
        mid = i - (j-i)/2
        
    maxL, minL = findminAndmax(arr, i, mid)
    maxR, minR = findminAndmax(arr, mid+1, j)
    
    if maxL < maxR:
        max = maxR
        
    else:
        max = maxL
        