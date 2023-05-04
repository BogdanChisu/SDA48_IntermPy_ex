"""
Pentru functii mici se foloseste cuvantul cheie lambda
"""

def square_of_number(x):
    return x * x

print(square_of_number(50))

varx = 50
# echivalent cu functia de mai sus
square_of_number_v2 = lambda x: x ** 2
print(square_of_number_v2(varx))

def capitalize_string(strx):
    return strx.upper()

strx = 'SDA 4 ever'
print(capitalize_string(strx))

capitalize_string_v2 = lambda strx: strx.upper()
print(capitalize_string_v2(strx))

items = list(range(1, 10))
# print(items)
#
#MAP
patrate = list(map(lambda x: x**2, items))
print(patrate)
#
# #FILTER
filtru = list(filter(lambda x: x%3, items))
print(filtru)

# print(sum(items))
# suma = 0
# for el in items:
#     suma += el
# print(suma)
print(f"max of items = {max(items)}")
print(f"min of items = {min(items)}")


date_json = {
    "studenti":[
        {"nume": "Ion",
         "prenume": "Ionescu",
         "adresa":{
             "oras": "Bucuresti",
             "strada": "Calea Victoriei",
             "numar": 123
         },
         "nr_tel": "40741752279"
         },
        {"nume": "Vasile",
         "prenume": "Petrescu",
         "adresa":{
             "oras": "Budapesta",
             "strada": "Calea Iobagilor",
             "numar": 123
         },
         "nr_tel": "40741752273"
         }
    ]
}