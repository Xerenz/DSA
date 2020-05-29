def partition(array, low, high):
	pivot = array[high]
	i = low - 1

	for j in range(low, high):
		if array[j] < pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
	i += 1
	array[i], array[high] = array[high], array[i]

	return i

def quicksort(array, high, low):
	if low < high:
		pos = partition(array, low, high)

		quicksort(array, low, pos-1)
		quicksort(array, pos+1, high)

if __name__ == '__main__':
	array = [55, 67, 23, 89, 104, 77, 2, 90]
	quicksort(array, 0, len(array)-1)
	print("Final array:", array)
