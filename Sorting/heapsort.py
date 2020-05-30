import time

def heapify(array, n, largest):
	print("  array in heapify state:", array)
	i = largest

	left = 2 * i + 1
	right = 2 * i + 2

	if left < n and array[left] > array[largest]:
		largest = left
	if right < n and array[right] > array[largest]:
		largest = right

	if i != largest:
		array[i], array[largest] = array[largest], array[i]
		print("    values passed to heapify-heapify:", array, n, largest)
		heapify(array, n, largest)

def heapsort(array):
	n = len(array)

	for i in range(n // 2 - 1, -1, -1):
		time.sleep(1)
		print("values passed to 1st heapsort-heapify:", array, n, i)
		heapify(array, n, i)
		time.sleep(1)
		print("array after 1st heapify:", array)

	for i in range(n-1, 0, -1):
		array[i], array[0] = array[0], array[i]
		time.sleep(1)
		print("values passed to 2nd heapsort-heapify:", array, i, 0)
		heapify(array, i, 0)

if __name__ == '__main__':
	array = [4, 10, 3, 5]
	heapsort(array)
	print("Sorted array:", array)