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
    if n == 2:
        return bool(n)
    dzielniki = 0
    if n/prime(n-1) == 0:
        dzielniki += 1
    if dzielniki == 2:
        return bool(n)
    else:
        return bool(None)
print(prime(4))
print("\n")

# print("--------ZADANIE 7-------")
# print("\n")
