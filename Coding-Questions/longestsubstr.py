def longest_unique_substr(string):
	seen = {}
	max_length = curr_length = head = 0

	for tail in range(len(string)):

		seen_index = seen.get(string[tail])

		if seen_index is not None and seen_index >= head:
			head = seen_index + 1

		curr_length = tail - head + 1
		max_length = max(max_length, curr_length)

		seen[string[tail]] = tail

	return max_length

if __name__ == '__main__':
	max_length = longest_unique_substr('bbb')
	print(max_length)