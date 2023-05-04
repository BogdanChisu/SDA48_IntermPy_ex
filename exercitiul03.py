"""
Exercitiul 3: Sa se creeze fisierul "numere_pare.json" care sa contina numerele pare
de la 1 pana la 100, folosind lambda
"""
import json
list_dict = []

even_numbers = list(filter(lambda x: x % 2 != 1, range(100)))

print(even_numbers)

with open('even_numbers.json', 'w') as file:
    json.dump(even_numbers, file)