class A:
	def funkcja(self):
		print("Jestem A")

class B(A):
	def funkcja(self):
		#A.funkcja(self)
		super().funkcja()
		print("Jestem C")

	def funkcja2(self):
		print("Jestem B")

b = B()
b.funkcja()
b.funkcja2()
