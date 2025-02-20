#CODIFICACIÓN DE SOFTWARE
#19/02/25
#Angel Aldahir Zarza Cintora
#Tuplas6.py

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Crear una tuple con 3 elementos: 10, "Hola" y 3.14
tupla = ("10, Hola, 3.14")
print(tupla)

#-------------------------------------------------------------------------#
#La tupla(1,2,3,4,5), accede y escribe el tercer element
tupla = (1,2,3,4,5)
element = 3 in (tupla)
print(element)

#-------------------------------------------------------------------------#
#Concatena las tuplas y almacena el resultado en una tupla Nueva
t1 = ('a', 'b', 'c')
t2 = (3, 2, 1)
tupla_final = t1+t2
print(tupla_final)

#-------------------------------------------------------------------------#
#Desempaqueta la tupla en tres variables y escribe sus valores
tupla = ('a','b','c')
var1 = tupla[0]
var2 = tupla[1]
var3 = tupla[2]
print(var1,var2,var3)

#-------------------------------------------------------------------------#
#verifica si el elemento 7 existe en la tupla (1,3,5,7,9)
tupla = (1,3,5,7,9)
existe = 7 in tupla
print(existe)

#-------------------------------------------------------------------------#
#crea una tupla (0,1,2,3,4,5) y escribe los elementos del indice 2 a 4 con slice
tupla = (0,1,2,3,4,5)
print(tupla[2:4])

#-------------------------------------------------------------------------#
#encuentra la longitude de una tupla (10,20,30,40,50)
tupla =  (10,20,30,40,50)
legth = len(tupla)
print(length)

#-------------------------------------------------------------------------#
#crea una tupla y repitela 3 veces
tupla = (1, 2, 3)
resultado = tupla*3
print(resultado)

#-------------------------------------------------------------------------#
#convierte la lista[1,2,3] a tupla
lista = [1, 2, 1, 3]
tupla = lista
print(tupla)

#-------------------------------------------------------------------------#
#Encuentra los valores minimo y maximo de la tupla(5,12,3,8,15)
tupla = (5,12,3,8,15)
valor_minimo = min(tupla)
valor_maximo = max(tupla)
print('Minimo: ',valor_minimo,' Maximo: ', valor_maximo) 


# In[116]:


tupla = (5,12,3,8,15)
valor_minimo = min(tupla)
valor_maximo = max(tupla)
print('Minimo: ',valor_minimo,' Maximo: ', valor_maximo) 

