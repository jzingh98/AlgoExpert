def bubbleSort(array):
	done = False
	counter = 0
    while not done:
		done = True
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				temp = array[i+1]
				array[i+1] = array[i]
				array[i] = temp
				done = False
		counter += 1
	return array
	
