import csv  
import random
header = ['X','Y']
data = []

with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(108):
        data=[random.randint(0,100),random.randint(0,100)]
        writer.writerow(data)