# def fun(n):
#     if n == 0:
#         return

#     print("Going:", n)

#     fun(n - 1)

#     print("Coming:", n)
# fun(3)

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(3))


# def sum_n(n):
#     if n == 0:
#         return 0
    
#     return n + sum_n(n-1)

# print(sum_n(5))

# def countdown(n):
#     if n == 5:
#         return
#     print(n)
#     countdown(n-1)
    
# countdown(10)


def countup(n):
    if n == 0:
        return
    print(n)
    countup(n-1)
    print(n)
    
countup(10)

#reverse a string:
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))