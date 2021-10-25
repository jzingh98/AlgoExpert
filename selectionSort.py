def selectionSort(array):
    # Write your code here.
	sorted = []
	while len(array) > 0:
		min = array[0]
		for i in array:
			if i < min:
				min = i
		sorted.append(min)
		array.remove(min)
    return sorted
