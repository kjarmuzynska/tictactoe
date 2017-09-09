import numpy as np

dirs = [ [1,-1], [1,0], [1,1], [0,1] ]
new_dirs=[]
for dir in dirs:
	for i in [2, 3, 4, 5]:
		new_dirs.append(dir*i)

print(new_dirs)
