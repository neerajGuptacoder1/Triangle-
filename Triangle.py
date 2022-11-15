# Neeraj Gupta Coder 
# Triangle Pattern

n = 10

for i in range(10):
	for j in range(i,n):
		print(" ",end=" ")
	for j in range(i+1):
		print(" * ",end=" ")
	print()