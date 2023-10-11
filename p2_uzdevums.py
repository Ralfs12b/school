# dēļu cena
a = "145" # par 1m kubā
s = "125" # par 1m kubā
t = 145
l = 125
# pati matemātika
x = str(input("Kāda ir dēļu šķira? a vai s:"))
h = int(input("Cik daudz dēļi ir pirkti:"))
b = float(input("Dēļa platums:"))
n = float(input("Dēļa biezums:"))
m = float(input("Dēļa garums:"))
j = b*n*m # tilpums
u = 1*1*1 # metrs kubā
p = ((j/u)*t)*h
o = ((j/u)*l)*h
def delis(): # funkcija
      if x == a:
            print(p)

      elif x == s:
            print(o)
#  Cik jāmaksā
print("Dēļu maksa būs:")
print(delis())
