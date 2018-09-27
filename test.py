def mything(x,y):
	x += x**2
	return x + y

x = input("Primer valor: ")
y = input("Segundo valor: ")

print("Resultado: " + str(mything(x,y)))