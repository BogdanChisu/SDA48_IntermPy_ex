"""
Cititi datele dintr-un fisier JSON numit "produse.json" si calculati pretul total
al produselor. Acest JSON ar trebui sa contina o lista de dictionare cu campurile:
"nume", "pret" si "cantitate".
"""
import json
with open('produse.json', 'r') as file:
    date_citite = json.load(file)

# print('\n')
# print(json.dumps(date_citite, indent=2))

total = 0
for elem in date_citite:
    total += elem["pret"] * elem["cantitate"]

print(f"Totalul produselor este: {total}")