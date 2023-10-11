# kas personai ir jāraksta
x = str(input("Darbinieka vārds:"))
y = int(input("Cik strādnieks ir daudz nostrādājis mēnesī(st):"))
a = float(input("Cik samaksā 1 st:"))
# pati funkcija
def alga():
      if a > 40:
            print(y*a*1.1)
      elif a < 40:
            print(y*a)
      else:
            print(y*a)
# ko persona redzēs kad visu ierakstīs
print(x)
print(alga())

