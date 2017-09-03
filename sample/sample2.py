variable_a = 2
variable_b = 3


def funckja1():
	variable_a = 4

def funckja2():
	global variable_a
	variable_a = 5


print(variable_a)
funckja1()
print(variable_a)
funckja2()
print(variable_a)
