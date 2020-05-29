import time

def factors(num):
	for i in range(1, num + 1):
		if num % i == 0:
			yield i # lazy evaluation

def infinite_fibonacci():
	a, b = 0, 1
	while True:
		yield a # lazy evaluation
		time.sleep(1)
		a, b = b, a + b

if __name__ == '__main__':
	for i in infinite_fibonacci():
		print(i)