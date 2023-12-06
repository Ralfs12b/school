import csv

arhivs = open('09112023.csv', 'r+')
lasītājs = csv.reader(arhivs, delimiter=".")
for ieraksts in lasītājs:
      Name = ieraksts[0]
      Does = ieraksts[3]
      print(f"(Name) - (Does)")
arhivs.close()
