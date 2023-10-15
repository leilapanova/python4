
# def distance(x1, y1, x2, y2):
#     res = ((x2 - x1)  2 + (y2 - y1)  2) ** 0.5
#     return res
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# print(distance(x1, y1, x2, y2))

# def fib(n)
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n - 2)
#     print(fib(int(input())))


# def power(a, n):
#     res = 1
#     if n > 0:
#         for i in range(n):
#             res *= a
#             return res
#     elif n < 0:
#         for i in range(-n):
#             res /= a
#             return res
#         return res
# print(power(int(input())))


# def is_year_leap(year):
#     if year % 4 != 0 or(year % 100 == 0 and year % 400 != 0):
#         return False
#     else:
#         return True
# print(is_year_leap(int(input())))


# def square(a):
#     p = 4*a
#     s = a*a
#     d = (a**2) / 2
#     d = d**0.5
#     x = (p, s, d)
#     return x
# print(square(int(input())))

# def season (month):
#     if month (1, 2, 12):
#         return "winter"
#     elif month in (3, 4, 5):
#         return "spring"
#     elif month in (6, 7, 8):
#         return "sunner"
#     elif month in (9, 10, 11):
#         return "autumn"
#     else:
#         return 'error'
#     print(season(int(input("month"))))


# def bank():
#     stavka = 10
#     n = int(input("Сколько у Вас денег?""\n"))
#     years = int(input("На сколько лет хотите сделать вклад?""\n"))
#
#     for i in range(years):
#         n = int(n+stavka*n/100)
#         print("По итогу вы получаете", n, "рублей")
# bank()


# def is_prime(a):
#     if a % a == 0 and a != 0:
#         return True
#     else:
#         return False
#
# a = int(input("Enter a number: "))
# print(is_prime(a))
#
# if year % 4 != 0:
#         return False
#     elif year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         return True
# def date(day, month, year):