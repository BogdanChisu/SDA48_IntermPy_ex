"""
Creati o functie care sa primeasca ca argument calea catre un fisier pickle care contine
o lista de cuvinte. Functia ar trebui sa filtreze lista cu ajutorul functiei filter()
si a unei functii lambda, astfel incat sa ramana doar cuvintele care au lungimea mai
mare decat 5 caractere. Afisati rezultatele.
"""
import pickle

cuvinte = ['abecedar', 'alfabet', 'github', 'pickle', 'ion', 'muratura', 'eu','teamwork']

with open('cuvinte.pickle', 'wb') as f:
    pickle.dump(cuvinte, f)

with open('cuvinte.pickle', 'rb') as f:
    words = pickle.load(f)

cuvinte_lungi = list(filter(lambda x: len(x) > 5, words))

print(cuvinte_lungi)
