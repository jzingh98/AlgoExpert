def getNthFib(n):
    # Write your code here.
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		value = recurse(3, 1, 1, n)
		return value

def recurse(i, a, b, n):
	if i == n:
		return b
	else:
		return recurse(i+1, b, a+b, n)
	
	
