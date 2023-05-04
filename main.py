try:
    print(5/0)
except ZeroDivisionError as e:
    print(f"Eroare: {e}")
finally:
    print('se executa indiferent daca trya  fost cu succes sau nu')

file_path = 'sda01.txt'

#not a best practice
f = open(file_path)
print(f.read())
f.close()

#best practice
with open(file_path, 'r') as f:
    print(f.read())

#serialization, stocare date din variable in fisiere
#1. pickle
#2. csv sau json