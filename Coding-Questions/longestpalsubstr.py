def longest_pal_substr(string):
	head = tail = 0

	substr = palstr = maxlenstr = ''

	for i in range(len(string)):
		substr = substr + string[i]
		palstr = string[i] + palstr

		if palstr == substr:	
			curstr = substr

		if len(curstr) > len(maxlenstr):
			maxlenstr = curstr

		print(substr, palstr)
			
	return maxlenstr

if __name__ == '__main__':
	max_length = longest_pal_substr('baabaabaabaab') 