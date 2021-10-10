# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    ans = recurse(1, array)
	return ans

def recurse(depth, array):
	tot = 0
	for item in array:
		if type(item) is int:
			tot += item
		else:
			special = recurse(depth+1, item)
			tot += special
	return tot*depth
