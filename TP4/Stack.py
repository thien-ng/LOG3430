class Node:

	def __init__(self, value):
		self.value = value
		self.next = None # the pointer initially points to nothing

	def __str__(self):
		return str(self.value)

class Stack : 
	# Initializes an empty stack.
	def __init__(self, max_size, max_trials, size_increment):
		self.first = None  # beginning of stack
		self.n = 0  # number of elements on stack
		self.max_size = max_size
		self.max_trials = max_trials
		self.size_increment = size_increment
		self.trials = 0

	# Returns true if this stack is empty.
	def isEmpty(self):
		return self.first == None

	# Returns true if this stack is full.
	def isFull(self):
		return self.n == self.max_size

	# Returns the number of items in this stack.
	def size(self):
		return self.n
	
	# Returns (but does not remove) item most recently added to this stack.
	def peek(self):
		if self.isEmpty():
			raise ValueError("Stack underflow")
		return self.first.value

	# Adds the item to this stack.
	def push(self, item):
		if self.isFull():
			self.trials += 1
			if self.trials == self.max_trials:
				self.max_size += self.size_increment
				self.trials = 0
			raise ValueError("Stack overflow")
		new_node = Node(item)
		if self.isEmpty():
			self.first = new_node
		else:
			new_node.next = self.first
			self.first = new_node
		self.n += 1
	
	# Removes and returns the item most recently added to this stack.
	def pop(self):
		if self.isEmpty():
			raise ValueError("Stack underflow")
		item = self.first.value
		self.first = self.first.next
		self.n -= 1
		return item
	
	# Returns a string representation of this stack (the sequence of items in this stack in LIFO order, separated by spaces)
	def __str__(self):
		result = "|"
		node = self.first
		while node:
			result += str(node.value) + "|"
			node = node.next
		return result
