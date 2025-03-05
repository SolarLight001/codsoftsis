{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "6dcee286-e46e-46f5-bbc6-d9b3b5c05c60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Introduce la ciudad:  Paris\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Torre Eifel\n"
     ]
    }
   ],
   "source": [
    "persona = input(\"Introduce la ciudad: \")\n",
    "\n",
    "ciudad = {\n",
    "'Delhi' : \"Red fort\",\n",
    "'Paris' : \"Torre Eifel\",\n",
    "'Nueva York' : \"Estatua de la Libertad\",\n",
    "'Rio de Janeiro' : \"Cristo Redentor\",\n",
    "}\n",
    "\n",
    "if persona in ciudad:\n",
    "    print(ciudad[persona])\n",
    "else:\n",
    "    print('no poseo tal informaCIÓN BASTARDO' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "313377ed-8bd1-4640-982c-f8067568f287",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "eres mayor de +18 años?:  -1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No esta aprobado para votar\n"
     ]
    }
   ],
   "source": [
    "pregunta = int(input(\"eres mayor de +18 años?: \"))\n",
    "\n",
    "if pregunta >= 18:\n",
    "    print('Aprobamos tu voto')\n",
    "else:\n",
    "    print('No esta aprobado para votar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "id": "3ae0c59c-09de-4fee-829a-3eae31acfaf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cesar 14 Martha: 65\n"
     ]
    }
   ],
   "source": [
    "edades = ('Martha: 65','Juan: 32', 'Cesar 14', 'Fatima: 89')\n",
    "print(min(edades), max(edades))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bcd13861-87eb-4a17-abab-d984549fce47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Pon tu numero:  73\n",
      "Otro numero?: (Y/N) y\n",
      "Pon tu numero:  86\n",
      "Otro numero?: (Y/N) No\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El numero menor será:  73\n"
     ]
    }
   ],
   "source": [
    "enable = True\n",
    "\n",
    "lista = []\n",
    "\n",
    "while(enable):\n",
    "    num1 = int(input('Pon tu numero: '))\n",
    "    lista.append(num1)\n",
    "    respuesta = input('Otro numero?: (Y/N)')\n",
    "    if respuesta == \"No\" or respuesta == 'n':\n",
    "        enable = False\n",
    "print(\"El numero menor será: \", min(lista))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
