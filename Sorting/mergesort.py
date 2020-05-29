def mergesort(array):
	if len(array) > 1:
		mid = len(array) // 2

		left = array[:mid]
		right = array[mid:]

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1
			else:
				array[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1


if __name__ == '__main__':
	array = [23, 43, 12, 1, 89, 56, 2]
	mergesort(array)
	print(array)