import random, csv 

with open('random_numbers.csv', mode ='w')as f:
      writer = csv.writer(f)
      writer.writerow(('random number'))
      for i in range(50):
            random_numbers = random.randint(0, 1000)
            writer.writerow((random_numbers))

f.close()
