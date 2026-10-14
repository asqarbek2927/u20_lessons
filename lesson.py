# int -> integer
# float
# str -> string
# bool -> boolean
# True False
# 0 1

# ism = "Asqar"
# age = 10
# kg = 60.5
#
# print(f"Ismi: {ism} Yoshi: {age} Kilosi: {kg}")
# print(age)
# print(kg)

# name = input("Ismingizni kiriting: ")
# age = int(input("Yoshingizni kiriting: "))
# print(name, age)

# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)
# print(a // b)
# print(a % b)

# 11 / 3 = 3.33333
# 11 // 3 = 3
# 95 % 3 = 2
# print(95%3)

# 2 ** 6
# 2 * 2 * 2 * 2 * 2 * 2

# 3 ** 10
# 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3


# 2 ** 2 -> kvadrat
# 2 ** 3 -> kub

# Foydalanuvchi son kiritadi uni kvadrat va kubini chiqaring.

# son = int(input("Son kiriting: "))
# print(son ** 2, son ** 3)


# Foydalanuvchi son kiritadi uni 6 darajasini chiqaring.
# son = int(input("Son kiriting: "))
# print(son ** 6)

# print(5**1)
# print(5**2)
# print(5**3)
# print(5**4)
# print(5**5)


#ball ozgaruvchi yarat va unga 25 qosh va 10ni ayirib tashla va 2 ga kopaytirib natijani chiqar.
# ball = 100
# ball += 25
# ball -= 10
# ball *= 2
# print(ball)

# a = 5
# b = 5

# print(a == b)
# print(a <= b)
# print(a != b)

# son = int(input("Son kiriting: "))
#
# print(son % 2 == 0)
# print(0 == 0)
# print(True)

# import requests
#
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
#     "latitude": 41.31,
#     "longitude": 69.28,
#     "current_weather": True
# }
# r = requests.get(url, params=params)
# print(r.url)
#
# ob_havo = r.json()["current_weather"]
# print(f"🌡 Harorat: {ob_havo['temperature']}°C")
# print(f"💨 Shamol: {ob_havo['windspeed']} km/soat")



# a=int(input("minut:"))
# print(a//2)
# print(a%2)


# requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/XYZ/").json()

# a=int(input("minut:"))
# print(a/60)

# olma = int(input("nech pul: "))
# banan = int(input("Sonini kiriting: "))
# print(olma * banan)
# # print(

# a=int(input("narx:"))
# b=int(input("narx:"))
# c=int(input("narx:"))
# print(a+b+c)

# a=int(input("narx:"))
# b=int(input("narx:"))
# c=int(input("narx:"))
# print(a+b+c/3)

# a=int(input("narx:"))
# b=int(input("narx:"))
# c=int(input("narx:"))
# summa = a + b + c
# print(summa/10 + summa)

# daqiqa = int(input("Daqiqani kiriting"))

# a=int(input("son kiriting: :"))
# b=int(input("son kriiting:"))
# print("========================")
# print(a + b)
# print("========================")



# daqiqa = int(input("Daqiqani kiriting"))
# print(f"{daqiqa / 60} soat boladi.")
#
#
# a=int(input("son kirit:"))
# b=int(input("son kirit:"))
# print()
# print(a+b)
# print("=" * 30)
# print(a-b)
# print("=" * 30)
# print(a*b)
# print("=" * 30)
# print(a**b)
# print("=" * 30)
# print(a/b)
# print("=" * 100)
# print(a//b)
# print("=" * 100)
# print(a%b)
# print("=" * 100)

# print("=" * 100)

# print("="a+b)

# b=int(input("tugilgan yilni yozin:"))
# print(b)
# print()


# b=int(input("yoshni yozin:"))
# print(b-2026)
# print(b<18)

# b=int(input("yoshni yozin:"))
# print(b-2026)
# print(b<18)

# b=int(input("tugilgan yilni kiriting:"))
# jami = 2026 - b
# print(jami >= 18)
# import os

# with open("log_file.txt", "w") as file:
#     file.write(f"xona saqlandi {}")



# class Author:
#     def __init__(self, name):
#         self.name = name
#
# a = Author("Asqar")
# class Book(Author):
#     def __init__(self, author_name, page):
#         self.author_name = author_name
#         self.page = page
# b = Book(a, 101)
# def student(name,age):
#     pass


# print("Assalomu aleykum")
# print("Xush Galdingiz")
# chek = 0
# while True:
#     buyurtma = int(input("""          Menu
#     1.Steyk 300 000
#     2.Osh
#     3.Non 10 000
#     4.Choy 5 000
#     5.Salat 10 000
#     0.Stop
#     tanlovizi kiriting:"""))
#     if buyurtma == 1:
#         print("Steyk buyurtmalarga qoshildi!")
#         chek += 300000
#     elif buyurtma == 2:
#         buyurtma2 = int(input("""            Tanlovlar royxati
#         1.Toy oshi 60000
#         2.Choyxona palov 80000
#         tanlovizi kiriting:"""))
#         if buyurtma2 == 1:
#             miqdor = int(input("Nechta buyurtma qilasiz?"))
#             chek += 60000 * miqdor
#             print("Toy oshi buyurtmalarga qoshildi!!!")
#         elif buyurtma2 == 2:
#             miqdor = int(input("Nechta buyurtma qilasiz?"))
#             chek+= 80000 * miqdor
#             print("Choyxona palovi buyurtmalarga qoshildi!!!")
#         else:
#             print("Togri tanlov kiriting!!!")
#     elif buyurtma == 3:
#         print("Non buyurtmalarga qoshildi!")
#         chek += 10000
#     elif buyurtma == 4:
#         print("Choy buyurtmalarga qoshildi!")
#         chek += 5000
#     elif buyurtma == 5:
#         print("Salat buyurtmalarga qoshildi!")
#         chek += 10000
#     elif buyurtma==0:
#         break
#     else:
#         print("Notogri tanlov qildingiz")
#
# if 500000 <= chek <= 999999:
#     chek *= 0.95
# elif 1000000 <= chek <= 1499999:
#     chek *= 0.90
# elif 1500000 <= chek:
#     chek *= 0.85
# print(f"Sizdan {chek} sum boldi")


