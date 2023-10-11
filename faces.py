import emoji
print(":) - :smiling_face: ")
print(":( - :Frowning_Face:")
x = str(input("Ievadi tekstu ar emoji, priekš emoji lieto CLDR saīsinājumu:"))
print(emoji.emojize(x))