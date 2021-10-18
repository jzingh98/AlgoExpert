def insertionSort(array):
	
    for i in range(1,len(array)):
		j = i
		k = i-1
		while k>=0 and array[k] > array[j]:
			temp = array[k]
			array[k] = array[j]
			array[j] = temp
			j -= 1
			k -= 1
	return array
