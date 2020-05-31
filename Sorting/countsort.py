def countsort(array):
	k = max(array)

	count_array = [0 for _ in range(k + 1)]

	for i in array:
		count_array[i] += 1

	print("initial count array:", count_array)

	for i in range(k):
		count_array[i + 1] = count_array[i] + count_array[i + 1]

	print("After increasing count:", count_array)

	new_array = [0 for _ in range(len(array))]

	for i in range(len(array)):
		element = array[i]
		index = count_array[element]
		if index < len(new_array):
			new_array[index] = element
			count_array[element] -= 1

	print("sorted array:", new_array)


if __name__ == '__main__':
	array = [1, 4, 1, 2, 7, 5, 2]
	countsort(array)