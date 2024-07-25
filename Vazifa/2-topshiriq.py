# TODO: Ushbu vazifani bajarish kerak
# FIXME: Xatoni to'g'irlang
# NOTE: Eslatma
import math

# ! Ushbu codni camentga olib yozilgan uni ishlatish uchun camentda ochib ishlatishingiz mumkin bo'ladi. 

# ? 22-misol
# a, b = 85, 99
# b, a = a, b
# print(f"a = {a} b = {b}")

# ? 23-misol
# a, b, c = 100, 200, 300
# a, b, c = c, a, b
# print(f"a = {a} b = {b} c = {c}")

# ? 24-misol
# a, b, c = 100, 200, 300
# a, b, c = b, c, a
# print(f"a = {a} b = {b} c = {c}")

# ? 6-misol
# a = 85
# S = a // 10 + a % 10 * 10
# print(f"O'nlar {a // 10} birlar: {a%10}")

# ? 7-misol
# a = 333
# S = 0
# S = a // 100 + a // 10 % 10 + a % 10
# print(S)

# ? 8-misol
# a = 85
# S = a // 10 + a%10*10
# print(S)

# ? 9-misol
# a = 755
# S = a // 100
# print(S)

# ? 10-misol
# a = 758
# print(f"O'nliklar: {a//10%10}  birliklar: {a%10}")

# ? 11-misol
# a = 778
# S = 0
# while a > 0:
#     S = S * 10 + a % 10
#     a //= 10
# print(f"Yig'indi: {S}")

# ? 12-misol
# a = 778
# S = a % 10 * 100 + a // 10 % 10 * 10 + a // 100
# print(f"Yig'indi: {S}")

# ? 13-misol
# a = 718
# S = a % 100 * 10 + a // 100
# print(f"Yig'indi: {S}")

# ? 14-misol
# a = int(input("Son kirit: "))
# S = a % 100 * 10 + a // 100
# print(f"Yig'indi: {S}")

# ? 15-misol
# a = 123
# S = a // 10 % 10 * 100 + a // 100 * 10 + a % 10
# print(f"Yig'indi: {S}")

# ? 16-misol
# a = 123
# S = a // 100 * 100 + a % 10 * 10 + a // 10 % 10
# print(f"Yig'indi: {S}")

# ? 17-misol
# a = 1531
# S = a // 100 % 10
# print(f"Yig'indi: {S}")

# ? 18-misol
# a = 1531
# S = a // 1000
# print(f"Yig'indi: {S}")

# ? 19-misol
# a = int(input("N kiriting: "))
# S = a // 60
# print(f"Minut: {S}")

# ? 20-misol
# a = int(input("N kiriting: "))
# S = a // 60 // 60
# print(f"Soat: {S}")

# ? 21-misol
# a = int(input("N kiriting: "))
# print(f"{a//60} minut {a%60} sekund")

# ? 22-misol
# a = int(input("N kiriting: "))
# soat = a // 60 // 60
# print(f"{soat} soat {a%60%60} sekund")

# ? 22-misol
# a = int(input("N kiriting: "))
# soat = a // 60 // 60
# print(f"{soat} soat {a%60%60} sekund")

# ? 23-misol
a = int(input("N kiriting: "))
soat = a // 60 // 60
minut = a // 60 - soat * 60
print(f"{soat} soat {minut} minut {a%60%60} sekund")
