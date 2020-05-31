def heapify(array, n, largest):
	i = largest

	left = 2 * i + 1
	right = 2 * i + 2

	if left < n and left > largest:
		largest = left
	if right < n and right > largest:
		largest = right

	if i != largest:
		array[i], array[largest] = array[largest], array[i]
		heapify(array, n, largest)

def heapsort(array):
	n = len(array)

	for i in range(n // 2 - 1, -1, -1):
		heapify(array, n, i)

	for i in range(n-1, 0, -1):
		array[i], array[0] = array[0], array[i]
		heapify(array, i, 0)

if __name__ == '__main__':
	array = [4, 10, 3, 5, 1]
	heapsort(array)
	print("Sorted array:", array)