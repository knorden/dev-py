import csv
import random
from random import seed
from random import randint

seed(1)

stock_types = ['Food', 'Book', 'Phone', 'Shoes', 'Toy', 'Kitchenware', 'Powertool', 'Appliance', 'Laptop', 'Gardentool', 'Plant']

with open ('data_src.csv', mode='w') as datout:
    datout = csv.writer(datout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# algorithm to randomly generate data:
    for _in in range(100):
        id = randint(0, 999)
        st_type = random.choice(stock_types)
        st = randint(0, 100)
        if (id < 1000):
            id = '{:03}'.format(id)
            id = str(id).zfill(4)
        datout.writerow([id, st_type, st])