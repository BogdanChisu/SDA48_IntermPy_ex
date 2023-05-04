"""
Creati un fisier json cu cheile număr și valorile pătratul său, de genul {1:1, 4:16} etc. Folositi lambda & context
managers.
"""
import json

elemente = list(range(1, 21))

elemente_la_patrat = list(map(lambda el: el**2, elemente))

squares_dict = {}
for index, l in enumerate(elemente):
    squares_dict[l] = elemente_la_patrat[index]

print(elemente_la_patrat)
print(squares_dict)

with open('square_file.json', 'w') as file:
    json.dump(squares_dict, file)

# #citirea din json
# fisier_json = 'square_file.json'
# with open(fisier_json, 'r') as file:
#     f_read = json.load(file)

