# y = []
# for i in range(0, 5):
#       print("Ievadi dec sk: ", i,)
#       item = float(input())
#       y.append(item)
#       y.reverse()
# print("Skaitļi:", y)
# print("Cik sk:", len (y))

# x = int(input("Ievadiet skaitli:"))
# for i in range(1, x + 1):
#       print(1, i*i*i)

# import math

# x = int(input("Ievadiet skaitli:"))
# for i in range(1, x + 1):
#       print(1, math.sqrt(i))

# x = int(input("Ieraksts skaitli: "))
# count = 0
# while x != 0:
#       x = x // 10
#       count = count + 1
# print("Ciparu skaits skaitlī ir: ", count)

# a = int(input("Ierakstat 1 sk: "))
# b = int(input("Ierakstat 2 sk: "))
# if a*b <= 1000:
#       print(a*b)
# else:
#       print(a+b)

# a = int(input("Ierakstat 1 sk: "))
# b = int(input("Ierakstat 2 sk: "))

# def s(a, b):
#       return a+b, a-b

# res = s(a, b)
# print(res)

a = int(input("Ierakstat 1 rādiusu: "))
b = int(input("Ierakstat 2 rādiusu: "))
p = 3.14
x = p*a**2
y = p*b**2

def laukums():
      return x, y

res = laukums(a, b)
print(res)


