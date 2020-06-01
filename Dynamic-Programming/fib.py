# solving fibonacci using the method of memoization
# the result of each function call is stored in an array

def fibonacci(n):
	f = [-1 for _ in range(n)]

	f[0], f[1] = 0, 1

	for i in range(2, n):
		f[i] = f[i-2] + f[i-1]

	return f[n-1]

if __name__ == '__main__':
	print(fibonacci(100))