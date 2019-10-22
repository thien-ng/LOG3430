class Node:

	def __init__(self, value):
		self.value = value
		self.next = None # the pointer initially points to nothing

	def __str__(self):
		return str(self.value)

class Queue : 
	MAX = 100
	# Initializes an empty queue.
	def __init__(self):
		self.first = None  # beginning of queue
		self.last = None  # end of queue
		self.n = 0  # number of elements on queue
		self.full = False  # indicates if the queue is full or not
		self.empty = True  # indicates if the queue is empty or not

	# Returns true if this queue contains one element.
	def hasOne(self):
		return self.n == 1

	# Returns true if this queue is empty.
	def isEmpty(self):
		return self.empty

	# Returns true if this queue is full.
	def isFull(self):
		return self.full

	# Returns the number of items in this queue.
	def size(self):
		return self.n
	
	# Returns the first item added to this queue 
	def check_first(self):
		if self.isEmpty():
			raise ValueError("Queue underflow")
		return self.first

	# Returns the last item added to this queue.
	def check_last(self):
		if self.isEmpty():
			raise ValueError("Queue underflow")
		elif self.hasOne():
			raise ValueError("Queue has only one element (the first one)")
		return self.last

	# Adds the item to this queue.
	def enqeue(self, item):
		if self.isFull():
			raise ValueError("Queue overflow")
		new_node = Node(item)
		if self.isEmpty():
			self.first = new_node
			self.empty = False
		elif self.hasOne():
			self.last = new_node
			self.first.next = self.last
		else:
			self.last.next = new_node
			self.last = new_node
			if self.n + 1 == Queue.MAX:
				self.full = True
		self.n += 1

	#Removes and returns the item on this queue that was least recently added.
	def dequeue(self):
		if self.isEmpty():
			raise ValueError("Queue underflow")
		item = self.first.value
		if self.hasOne():
			self.first = None
			self.empty = True
		elif self.n == 2:
			self.first = self.last
			self.last = None #to avoid loitering
		else:
			self.first= self.first.next
		self.n -= 1
		self.full = False
		return item