x = input("Uzraksti faila nosaukumu ar tipu:") # raksta failu
def atpazin():  # funkcija kas atpazin failu
      if x == ".png , .gif , .bmp":  # ar faila gala tipu nosaka tipu
            print("šis ir attēls")
      elif x == ".txt , .doc , .pdf":  # ar faila gala tipu nosaka tipu
            print("šis ir teksta documents")
      else:
            print("fails nav atpazīts")

print(atpazin()) # izraksta faila tipu uz ekrāna
