#!/usr/bin/env python
# coding: utf-8

# In[128]:


#-----------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales.
for i in range(10):
    print(i)

#-----------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros impares.
for i in range(1, 20, 2):
    print(i)
#-----------------------------------------------------------------------------#
#Escribe un programa que imprima los primeros 10 numeros naturales en orden descendente.
for i in range(10, 1, -1):
    print(i)
#-----------------------------------------------------------------------------#
#Escribe un programa que escriba la tabla de multiplicar de un numero especificado por el usuario5
ent = int(input("Escribe un número: "))
num = 0
for num in range(10):
    print(num*ent)

#-----------------------------------------------------------------------------#
#Esribir un programa que escriba el producto de los digitos de un numero especificado por el usuario.
num = input("tu numero bastardo: ")
lista = list(num)
nt = 1
print(lista)

for x in lista:
    nt = nt * int(x)
    print(x)
print(nt)

    

