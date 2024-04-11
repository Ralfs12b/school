

class Transports:
    def __init__(self, marka, maxAtrums, nobraukums, dzimis):
        self.marka = marka
        self.maxAtrums = maxAtrums
        self.nobraukums = nobraukums
        self.dzimis = dzimis

    def vecums(self):
        return 2024 - int(self.dzimis)
        

    # def Transport(self):
    #     print("Marka ir: " + self.marka)
    #     print("Maksimālais ātrums KM: " + str(self.maxAtrums))
    #     print("Nobraukums KM: " + str(self.nobraukums))

class Autobuss(Transports):
    pass

# r1 = Transports("Opels", 189, 8756)

p = Autobuss("Opels", 124, 3643, 1991)
print(p.marka, p.maxAtrums, p.nobraukums, p.dzimis)