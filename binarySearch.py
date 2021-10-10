def binarySearch(array, target):
	start = 0
	end = len(array) - 1
	while start < end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
	if array[start] == target:
		return start
	else:
    	return -1
