# dd = {}
# ee = dict()
# # len nosaka garumu
# print(dd, len(dd), type(dd))
# print(ee, len(ee), type(ee))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 3455,
#   "colors": ["red", "blue"]
# }
# print(thisdict)
# print(thisdict["brand"])
# print(thisdict["year"])
# # 3 jo year atkārtojās
# print(len(thisdict))

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2343

# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020
# print(x) #after the change

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# atslēga = {"desmit", "divdesmit", "trīsdesmit"}
# vērtības = {10, 20, 30}
# x = zip(atslēga, vērtības)
# print(tuple(x))

vērtējumi = {
      "klase": {
            "skolēns": {
                  "vārds": "Mikus",
                  "atzīmes": {
                        "fizika": 8,
                        "vēsture": 7,
                        "matemātika": 9
                  }
            }
      }
}

print(vērtējumi["klase"]["skolēns"]["atzīmes"]["fizika"])