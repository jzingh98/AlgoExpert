def findThreeLargestNumbers(array):
	first3 = array[0:3]
    first = max(first3)
	first3.remove(first)
	second = max(first3)
	first3.remove(second)
	third = first3[0]
	
	for item in array[3:]:
		# Check if it's the biggest item
		if item > first:
			third = second
			second = first
			first = item
		# Check if it's the second biggest item
		elif item > second:
			third = second
			second = item
		# Check if it's the third biggest item
		elif item > third:
			third = item
	return [third, second, first]
