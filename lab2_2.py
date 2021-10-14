print("--------ZADANIE 1--------")
class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return self.side * 4

kwadrat1 = square(4)
kwadrat2 = square(5)

print(kwadrat1.area())
print(kwadrat2.perimeter())
print("\n\n")

print("--------ZADANIE 2--------")
class traingle:
    def __init__(self, side, height):
        self.side = side
        self.height = height
    def area(self):
        return (self.side * self.height) * 0.5
    def perimeter(self):
        return self.side * 3

trojkat1 = traingle(2,3)
trojkat2 = traingle(4,5)

print(trojkat1.area())
print(trojkat2.perimeter())
print("\n\n")

# print("--------ZADANIE 3--------")
# i = 0
# kw = []
# while i != 10:
#     x = input("podaj bok o dlugosci 11-20: ")
#     x = int(x)
#     if (x >= 11) & (x <= 20):
#         x = square(x)
#         kw.append(x)
#         i += 1
#     else:
#         print("zla liczba, sprobuj jeszcze raz")
# # print(kw)
# for j in kw:
#     print("pole kwadratu:", j.area(), " obwod kwadratu:", j.perimeter())

m = 0
troj = []
while m != 1:
    x = input("podaj bok o dlugosci 6-10: ")
    x = int(x)
    if (x >= 6) & (x <= 10):
        # y = input("podaj wysokosc o dlugosci 15-19: ")
        # y = int(y)
        #     if (y >= 15) & (y <= 19):
        #     else:
        #         print("zla liczba, sprobuj jeszcze raz")
     t = traingle(x, x)
     m += 1
    else:
        print("zla liczba, sprobuj jeszcze raz")

n = 0
while n != 1:
        y = input("podaj wyskosc o dlugosci 15-19: ")
        y = int(y)
        if (y >= 15) & (y <= 19):
            n += 1
        else:
            print("zla liczba, sprobuj jeszcze raz")

t = traingle(x, y)
troj.append(t)
print(troj)