#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-----------------------------------------------------------------------#
#Escribe un programa que calcule el numero factorial de una cantidad definida por el usuario.
num = 5
factorial = 1
for i in range(1, num +1):
    factorial = i*factorial
print(factorial)

#-----------------------------------------------------------------------#
#Escribir un programa que muestre la suma de los digitos de un numero definido por el usuario.
variable = input("tu numero aqui --> ")
lista = list(variable)
nt = 0
for x in lista:
    nt = nt + int(x)
    print(x)
print(nt)

#-----------------------------------------------------------------------#
#Escribir un programa que acepte 10 numeros separados por comas y calcular su promedio.
num = input("Dame 10 números al azar: ")
Lnum = num.split(',')
for nb in Lnum:
    lista = lista.append(int(nb))
print(avg(lista))
#-----------------------------------------------------------------------#
#Escribir un programa que escriba todos los numeros primos que se encuentren entre dos numeros escritos por el usuario.
primos = int(input("Escribe 2 números--> "))
for primos in range (start, end):
    if primos%2!=0:
        print(primos)
#-----------------------------------------------------------------------#
#Escribir un programa que escriba el siguiente formato hasta un numero definido por el usuario:
#Ejemplo;
#1
#12
#123
#1234
#12345
#123456
#******
#*****
#****
#***
#**
#*

pregunta = input('Escriba porfavor, me aburro XD: ')
