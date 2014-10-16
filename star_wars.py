#! /usr/bin/python

#Questions
print "Hola, mi joven padawan. Creo que necesitaras un nombre en condiciones si aspiras a ser un caballero Jedi."
name = raw_input("Cual es tu nombre de pila?: ")
print "Suena bien..."

surname = raw_input("Cual es tu apellido?: ")
print "Ya veo..."

momname = raw_input("Cual es el apellido de soltera de tu madre?: ")
print "Interesante..."

city = raw_input("En que ciudad naciste?: ")
print "Bonito lugar..."

print "Pensando..."

#Lower-case the answers
name = name.lower()
surname = surname.lower()
momname = momname.lower()
city = city.lower()

#Now, proceed with the Star Wars Name.
#Source: http://infostarwars.wordpress.com/2013/05/13/tu-nombre-en-star-wars/

star_name = surname[0:3] + name[0:2]
star_surname = momname[0:2] + city[0:3]
star_wars_name = star_name + " " + star_surname

print "Tu nuevo nombre es %s" % (star_wars_name.title())
print "Que la Fuerza sea contigo."