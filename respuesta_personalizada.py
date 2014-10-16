#! /usr/bin/python

print "Bienvenido al programa de respuesta personalizada."
name = raw_input("Cual es tu nombre? ")

if len(name) == 0 or name.isdigit():
	print "En realidad SI tienes que escribir tu nombre (el de pila), prueba otra vez"
	name = raw_input("Cual es tu nombre? ")
#elseifs commented. Want to give personal messages with 'in'.
#elseif name in [luis, Luis, LUIS]:
#	print "Hola Luis. Tu nombre me hace indicar que eres un mambru. No lo niegues."
#elseif name in [jorge, Jorge, JORGE]:
#	print "Tu cara me suena. Bienvenido, maestro."
else:
	print "Encantado de conocerte, %s. Conozcamonos mejor." % name