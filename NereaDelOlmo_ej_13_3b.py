#!/usr/bin/python
# -*- coding: utf-8 -*-

# Autor: Nerea Del Olmo Sanz
# Ej: 13.3.- Tablas de multiplicar


print "\nTablas de Multiplicar\n---------------------"

numbers = range(11)

for number_i in numbers:
	print "\nTabla del " + str(number_i) + "\n------------"
	for factor_i in numbers:
		multiplication = number_i * factor_i 
		print str(number_i) + " por " + str(factor_i) + " es " + str(multiplication)
	
