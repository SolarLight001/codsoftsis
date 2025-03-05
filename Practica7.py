#!/usr/bin/env python
# coding: utf-8

# In[5]:


#-------------------------------------------------------------------------#
#Escribir un programa que acepte el porcentaje de un alumno y evalue el grado de acuerdo al siguiente criterio
#Calificacion	Grado
#   >90				A
#   >80 y <= 90		B
#   >=60 y <=80		C
#   menor a 60		D
porciento = float(input("Escribe el porcentaje del Alumno ---> "))
if porcentaje > 90:
    grado = 'A'
    print(f"El grado del alumno será: {grado}")
elif porciento > 80 and porciento <= 90:
    grado = 'B'
    print(f"El grado del alumno será: {grado}")
elif porciento >= 60 and porciento <= 80:
    grado = 'C'
     print(f"El grado del alumno será: {grado}")
else: 
    grado = 'D'
     print(f"El grado del alumno será: {grado}")

#-------------------------------------------------------------------------#
#Escribir un programa que capture el precio de una bicicleta y muestre los impuestos que debe pagar siguiendo los criterios siguientes:
# Costo					Impuesto
# >100000				15%
# >50000 y <= 100000	10% 
#<=50000				 5%

precio_de_scooter = float(input("Escribe el precio de la bici: "))
if precio_de_scooter > 100000:
    IVA = precio_de_scooter * 0.15
    print(f"El IVA a pagar por el scooter será de: {IVA}")
elif  precio_de_scooter > 50000 and precio_de_scooter <= 100000:
    IVA = precio_de_scooter * 0.10
     print(f"El IVA a pagar por el scooter será de: {IVA}")
else:
    IVA = precio_de_scooter * 0.05
     print(f"El IVA a pagar por el scooter será de: {IVA}")

#-------------------------------------------------------------------------#
#Escribir un programa que verifique si un año es bisiesto o no
bisiesto = float(input("Escribe el año que quieres saber si es bisiesto: "))
if (bisiesto % 4 == 0 and (año % 100 != 0 or año % 400 == 0))
    print(f"El año {bisiesto} no es bisiesto. ")
else: 
    print(f"El año {bisiesto} es bisiesto")

#-------------------------------------------------------------------------#
#Escribir un programa que capture un numero del 1 al 7 y muestre el nombre del dia de la semana
#Por ejemplo el 1 seria Domingo y el 2 Lunes
num_dia = int(input("Ingresa un número del 1 al 7 ==> "))
dias = "Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"
if 1 <= num_dia <= 7:
    print(f"El día {num_dia} es {dias[num_dias]}")
else:
    print("Número fuero de rango o no encontrado!!")

#-------------------------------------------------------------------------#
#Escribir un programa que acepte un numero del 1 al 12 y muestre el nombre del mes asi como los dias que contiene
#Ejemplo 1 seria Enero tiene 31 dias
num_meses = int(input("Ingresa un número del 1 al 12 ==> "))
meses = "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
if 1 <= num_meses <= 12:
    print(f"El día {num_meses} es {meses[num_meses]}")
else:
    print("Número fuero de rango o no encontrado!!")

