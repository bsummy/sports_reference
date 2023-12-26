#!/usr/bin/env python3
import json
import sys
from tabulate import tabulate
import importlib

# an attempt to be a bit defensive with the filename
# if you include a command line arg, it'll use that. 
if len(sys.argv) != 2:
    json_file = "sr.json"
else:
    json_file = sys.argv[1]

with open(json_file, "r") as file:
    data = json.load(file)

table = [["TM"]]
for index, team in enumerate(data):
    row = [team] # adding side header
    for opp_index, opp in enumerate(data[team]):
        if opp_index == index: # self reference dashes
            row.append("--")

        # only print wins since CHC wins against CIN == CIN losses against CHC
        # if we lost trust in a data source, you could cross reference them for discrepencies
        row.append(data[team][opp]["W"])

    table[0].append(team)
    table.append(row)

row.append("--") # adding the final dashes
table.append(table[0])  # adding the header to the last row

# using a module to print, but if you don't have it installed you can just see the data from array form
try:
    importlib.import_module('tabulate')
    print(tabulate(table[1:], headers=table[0], tablefmt='grid', colalign=['center']*len(table[0])))
except ImportError:
    print('tabulate is not installed. Please run: `pip install tabulate` to see full results')
    for row in table:
        print(row)
