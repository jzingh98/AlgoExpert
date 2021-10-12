def isValidSubsequence(array, sequence):
    for element in array:
		curr_comparator = sequence[0]
		if element == curr_comparator:
			sequence.remove(element)
		if len(sequence) == 0:
			return True
	else:
		return False
