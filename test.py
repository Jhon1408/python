#Cambio pendejo para probar algo.
#Pues si wey no mames, xddd
class Animal():
	"""docstring for Animal"""
	def __init__(self, color, name):
		self.color = color
		self.name = name
	def bark(self, func):
		print(str(self.name) + "({}) ".format(str(self.color)) + "is Barking: " + func)

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, loud):
		if loud == "si" or loud == "Si" or loud == "SI":
			self.loud = True
		else:
			self.loud = False
	def getBark(self):
		if self.loud ==  True:
			return("WOOF!")
		else:
			return("Woof!")
	def say(self):
		self.bark(self.getBark())

Fido = Dog(input("Tu perro es ruidoso: "))
Fido.name = input("Escribe el nombre de tu perro: ")
Fido.color = input("Escribe el color de tu perro: ")
Fido.say()
