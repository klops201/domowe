# print("--------ZADANIE 1--------")
# def numbers(n):
#     if n == 0:
#         print(0)
#         return 0
#     else:
#         print(n)
#         return numbers(n-1)
# numbers(10)
# print("\n")

# print("--------ZADANIE 2-------")
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(11))
# print("\n")

# print("--------ZADANIE 3-------")
# def power(number, n):
#     if n == 0:
#         return 1
#     else:
#         return number * power(number,n-1)
# print(power(3,4))
# print("\n")

# print("--------ZADANIE 4-------")
# def reverse(txt):
#     string = str(txt)
#     if len(string) == 0:
#         return
#     else:
#         reverse(string[1:])
# print(reverse("jedziem"))
# print("\n\n")
# def reverse(string):
#     if len(string) == 0:
#         return
#
#     temp = string[0]
#     reverse(string[1:])
#     print(temp, end='')
# print(reverse("jedziem"))

# print("--------ZADANIE 5-------")
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))
# print("\n")

print("--------ZADANIE 6-------")
def prime(n):
    i = 2
    if n == 2:
        return bool(1)
    if i + 1 == n:
        return bool(1)
    if n <= 2 and n > 0:
        return bool(None)
    if n % i == 0:
        return bool(None)
    i += 1
    return prime(n)
print(prime(19))
print("\n")

# print("--------ZADANIE 7-------")
# print("\n")
