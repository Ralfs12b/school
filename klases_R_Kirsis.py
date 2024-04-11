

class Kalkulators: # Veidojās paša klase - Kalkulators

    def __init__(self, a, b):  
        self.a = a
        self.b = b 

    def skait(self):
        return self.a + self.b # Saskaitīšana
    
    def atnem(self):
        return self.a - self.b # Atņemšana
    
    def reiz(self):
        return self.a * self.b # Reizināšana
    
    def dal(self):
        return self.a / self.b # Dalīšana
         
a = int(input("Ieraksti savu pirmo skatli: ")) # Raksta 1 skaitli
b = int(input("Ieraksti savu otro skatli: ")) # Raksta 2 skaitli
g=Kalkulators(a,b)
while True: 
    def menu():
        x = ('Rakstot ciparu: 1. Saskaitīt 2. Atņemt 3. Reizināt 4. Dalīt') # Izvēles cipari
        print(x)
    menu()
    Izvele = int(input("Ierakstiet skaitli(1-4): ")) # Tiek prasīts uzrakstīt ciparu, priekš atbildes uzzināšanas
    if Izvele == 1:
        print("Jūsu iznākums ir (saskaitīšana) :", g.skait()) # Izvēloties 1 būs tikta veikta saskaitīšana
    elif Izvele == 2:
        print("Jūsu iznākums ir (atņemšana) :", g.atnem()) # Izvēloties 2 būs tikta veikta atņemšana 
    elif Izvele == 3:
        print("Jūsu iznākums ir (reizināšana) :", g.reiz()) # Izvēloties 3 būs tikta veikta reizināšana
    elif Izvele == 4:
        print("Jūsu iznākums ir (dalīšana) :", g.dal()) # Izvēloties 4 būs tikta veikta dalīšana
    else:
        print("IR RADUSIES KĻŪDA MĒĢINIET VELREIZ IERAKSTĪT CIPARU NO 1 LĪDZ 4") # Ja ieraksta jebko citu tad radīsiesz kļūda







