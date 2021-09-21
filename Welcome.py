from sys import addaudithook


print("Hello World")

'''Zmienna int'''

liczba = 2
print(type(liczba))

'''Zmienna float'''

liczba2 = 2.3
print(type(liczba2))

'''Łamanie stringa na kilka linijek i wypisanie jej'''

nazwa = """
Ziom
son
koxik
"""

print(nazwa)
print(type(nazwa))

'''Wartość true false'''

prawda = True
print(type(prawda))

'''Wartość null'''

nic = None
print(type(nic))

'''Zdefiniowanie wartości zmiennych'''

imie = "Adam"
wiek = 32

'''Wrzucemoe zmiennej do stringa w cudzyslowiu'''

messege = f"Wiek {wiek} imie {imie}"
print(messege)
print(type(messege))

'''Wrzucenie zmiennej do stringa poza cudzyslowiem'''

messege2 = "Wiek {} imie {}".format(wiek, imie)
print(messege2)

'''Zamiana bool na stringa'''

nic2 = True
print(type(nic2))
print(nic2)
nic3 = str(nic2)
print(nic3)
 
'''Zamiana stringa na float'''

cos = "2.0"
print(type(cos))
cos2 = float(cos)
print(type(cos2))
print(cos2)


lista = ["adam", 23, True, None]
print(lista[0])
print(lista[-1])
print(lista[0:3])
print(lista)

'''Wycinanie z listy fragmentów'''
print(lista[::-1])



imie2 = "Adam"
print(imie2[0:3])
print(imie2[::-1])
'''Odwrócenie imieenia'''



lista2 = ["Nikt", 2, 23, 3, 5.4 ,None, [1 ,2]]
lista2.insert (1,3) 
'''Dodanie zmiennej do listy najpierw pozycja potem wartość'''

print(lista2)

print(len(lista2))
'''Wartość  [...[1, 2]] jest liczona jako jedna długość'''

lista2.remove (2)
'''usunięcie zmiennej z listy'''

print(lista2)

sus = lista2.remove (5.4)
print(sus)
'''Wyświetlenie wartości zmiennej która usuwała inną wartość'''

print(lista2[-1])
