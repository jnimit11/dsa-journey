def findfactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * findfactorial(n-1)
n = 4
result = findfactorial(n)
print("the factorial of the given number is:", result)