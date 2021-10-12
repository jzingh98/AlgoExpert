def sortedSquaredArray(array):
	# Determine the split index and split lists O(N)
	countneg = 0
	for i in array:
		if i < 0:
			countneg += 1
	lower = array[0:countneg]
	upper = array[countneg:]
	
	# Reverse the lower list O(N)
	lower.reverse()
	
	# Merge lower and upper lists O(N)
	answer = []
	while len(lower) > 0 and len(upper) > 0:
		if(abs(lower[0]) < abs(upper[0])):
			answer.append(lower[0])
			lower.remove(lower[0])
		else:
			answer.append(upper[0])
			upper.remove(upper[0])
	if len(upper) > 0:
		answer.extend(upper)
	if len(lower) > 0:
		answer.extend(lower)
		
	#Square each element O(N)
	answer2 = [x*x for x in answer]
	return answer2
		
	
