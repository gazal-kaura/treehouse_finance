def exists(x):
	if x:
		return True
	else:
		return False

x = None
print("Checking existance of Undefined Variable")
print(exists(x))
x = 1
print("Checking existance of Defined Variable")
print(exists(x))
