"""Shuffle the fields in each row and write them to a file.
"""

import csv
import random

infilename = "C:\Users\aaron\Downloads\ford_escort.csv"
outfilename = "ford_scrambled.csv"

csv_in = open(infilename, 'r')
csv_out = open(outfilename, 'w')

spamreader = csv.reader(csv_in) 
spamwriter = csv.writer(csv_out)

for row in spamreader:
    random.shuffle(row)
    spamwriter.writerow(row)



