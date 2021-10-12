def nonConstructibleChange(coins):
	coins.sort()
    change = 0
	for item in coins:
		if item - change > 1:
			return change + 1
		else:
			change += item
	return change + 1
