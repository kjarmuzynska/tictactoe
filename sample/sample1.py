class A:
	def funkcja(self):
		print("Jestem A")

class B:
	def funkcja2(self):
		print("Jestem B")

a = A();
a.funkcja()

b = B();
b.funkcja2()

lista = [a, b]

for obiekt in lista:
	obiekt.funkcja()
