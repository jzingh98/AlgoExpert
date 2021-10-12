def twoNumberSum(array, targetSum):
    my_dict = {}
	for item in array:
		difference = targetSum - item
		if difference in my_dict.keys():
			return [difference, item]
		my_dict[item] = difference
	return[]
