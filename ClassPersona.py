import datetime



class Persona:
    def __init__(self, vards, valsts, dzimis):
        self.vards = vards
        self.valsts = valsts
        self.dzimis = dzimis

    def introduce_self(self):
        print("Sveiki mans vārds ir: " + self.vards)
        print("Esmu no: " + self.valsts)
        print("Esmu dzimis: " + str(self.dzimis))

x = datetime.datetime(2005, 3, 24, 20, 34, 53)
x2 = datetime.datetime(2005, 5, 31, 21, 53, 44)
x3 = datetime.datetime(2006, 4, 23, 2, 34, 53)
x4 = datetime.datetime(2006, 8, 22, 4, 24, 13)
x5 = datetime.datetime(2006, 4, 19, 8, 14, 54)

r1 = Persona("Toms", "Īrija", x2)
r2 = Persona("Ralfs", "Latvija", x)
r3 = Persona("Uvis", "Latvija", x3)
r4 = Persona("Jānis", "Latvija", x4)
r5 = Persona("Rihards", "Latvija", x5)


r1.introduce_self()
r2.introduce_self()
r3.introduce_self()
r4.introduce_self()
r5.introduce_self()