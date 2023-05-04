"""
Scrieti un program care sa extraga datele dintr-un fisier JSON numit "studenti.json"
si sa le salveze in alt fisier numit "studenti_promovati.json", pastrand doar studentii
cu nota mai mare sau egala cu 5. Folositi functii lambda, context managers si exception
handling try except.
"""

import json

try:
    with open('studenti.json', 'r') as file:
        date_note = json.load(file)
        lista_promovati = list(filter(lambda x: x["nota"] >= 5, date_note))
        print(lista_promovati)
except Exception as e:
    print(f"Eroare la accesarea fisierului, {e}")

try:
    with open('studenti_promovati.json', 'w') as file:
        json.dump(lista_promovati, file)
except Exception as e:
    print(f"Eroare la scrierea in fisier, {e}")