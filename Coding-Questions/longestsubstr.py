def longest_unique_substr(string):
	seen = {}
	max_length = head = 0

	sub = ''

	for tail in range(len(string)):

		seen_index = seen.pop(string[tail], None)

		if seen_index is not None:
			max_length = max(max_length, tail - head)
			head = seen_index + 1
			print(sub)
			sub = sub[head:tail]
		else:
			max_length = tail - head
			sub += string[tail]
			seen[string[tail]] = tail

	return max_length

if __name__ == '__main__':
	max_length = longest_unique_substr('elizabethgeorge')
	print(max_length)