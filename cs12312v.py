import csv
 
# opening the CSV file
with open('video2_opendata.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    print(lines)