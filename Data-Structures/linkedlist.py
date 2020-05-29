import time

class Link():

	def __init__(self, data):
		self.data = data
		self.next = None

	def show(self):
		print(self.data)

class LinkedList():

	def __init__(self, root=None):
		self.root = root
		self.tail = None
		self.length = 0

		if self.root:
			self.tail = self.root
			self.length += 1

	def append(self, node):
		if not self.root:
			self.root = node
			self.tail = self.root
		else:
			self.tail.next = node
			self.tail = self.tail.next
		self.length += 1

	def print_list(self):
		curr = self.root
		while curr:
			print(curr.data)
			time.sleep(1)
			curr = curr.next

def mergesort(array):
	mid = array.length // 2
	i = 0

	while i < mid:
		curr = array.root
		curr.show()
		curr = curr.next
		i += 1 

if __name__ == '__main__':
	array = [23, 43, 1, 22, 9]
	p = LinkedList()
	for i in array:
		p.append(Link(i))
	p.print_list()
	mergesort(p)


























