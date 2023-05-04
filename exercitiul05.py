"""
Creati un fisier JSON apoi cititi datele din "angajati.json" ce contine o lista de
angajati, sub forma unor dictionare cu campurile: "nume", "varsta" si "salariu".
Calculati salariul mediu al angajatilor, folosind o functie lambda si functia map().
"""

import json
with open('angajati.json', 'r') as file:
    date_salar = json.load(file)

salarii = list(map(lambda x: x["salar"], date_salar))
print(sum(salarii) / len(salarii))