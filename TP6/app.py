import random as rand
import abc

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None # the pointer initially points to nothing

	def __str__(self):
		return str(self.value)

class List : 
	# Initializes an empty list.
	def __init__(self):
		self.list = []		
		self.n = 0  # number of elements on list

	# Returns true if this list is empty.
	def isEmpty(self):
		return self.n == 0

	# Returns the number of items in this list.
	def size(self):
		return self.n
	
	# Returns the first item added to this list 
	def check(self):
		if self.isEmpty():
			raise ValueError("list underflow")
		return self.list[0]
	
	#Removes and returns the first item in the list
	def peek(self):
		if self.isEmpty():
			raise ValueError("list underflow")
		item = self.list.pop(0)
		self.n -= 1
		return item

	def append(self, item):
		self.list.append(item)
		self.n += 1

	def prepend(self, item):
		if self.isEmpty():
			self.list.append(item)
		else:
			self.list.insert(0, item)
		self.n += 1

	def accept(self, visitor):
		visitor.visit(self)

class Queue(List): 

	# Initializes an empty queue.
	def __init__(self, max_size,  *args, **kwargs):
		self.max_size = max_size
		super(Queue, self).__init__(*args, **kwargs)

	def isFull(self):
		return self.n == self.max_size

	# Adds the item to this queue.
	def enqueue(self, item):
		if self.isFull():
			raise ValueError("Queue overflow")
		self.append(item)

	#Removes and returns the item on this queue that was least recently added.
	def dequeue(self):
		try:
			return self.peek()
		except ValueError:
			print("Queue underflow")

class Stack(List): 
	# Initializes an empty stack.
	def __init__(self, max_size, *args, **kwargs):
		self.max_size = max_size
		super(Stack, self).__init__(*args, **kwargs)

	# Returns true if this stack is full.
	def isFull(self):
		return self.n == self.max_size

	# Adds the item to this stack.
	def push(self, item):
		if self.isFull():
			raise ValueError("Stack overflow")
		self.prepend(item)
	
	# Removes and returns the item most recently added to this stack.
	def pop(self):
		try:
			return self.peek()
		except ValueError:
			print("Stack underflow")

class AutoAdaptiveStack(Stack): 

	def __init__(self, max_trials, size_increment, *args, **kwargs):
		self.max_trials = max_trials
		self.size_increment = size_increment
		self.trials = 0
		self.rejected = Queue(4) 
		super(AutoAdaptiveStack, self).__init__(*args, **kwargs)

	def push(self, item):
		try:
			super(AutoAdaptiveStack, self).push(item)
		except:
			print("There is no free space actually :( try later")
			self.trials += 1
			try:
				self.rejected.enqueue(item)
			except: 
				print("There is no free space in the rejected items' queue")
			if self.trials == self.max_trials:
				self.max_size += self.size_increment
				self.trials = 0
				while (not self.isFull or not self.rejected.isEmpty()):
					self.prepend(self.rejected.dequeue())

class AutoAdaptiveQueue(Queue): 

	def __init__(self, max_trials, size_increment, *args, **kwargs):
		self.max_trials = max_trials
		self.size_increment = size_increment
		self.trials = 0
		self.rejected = Queue(4) 
		super(AutoAdaptiveQueue, self).__init__(*args, **kwargs)

	def enqueue(self, item):
		try:
			super(AutoAdaptiveQueue, self).enqueue(item)
		except ValueError:
			print("There is no free space actually :( try later")
			self.trials += 1
			try:
				self.rejected.enqueue(item)
			except: 
				print("There is no free space in the rejected items' queue")
			if self.trials == self.max_trials:
				self.max_size += self.size_increment
				self.trials = 0
				while (not self.isFull or not self.rejected.isEmpty()):
							self.prepend(self.rejected.dequeue())
							
class Printer(object, metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name

	def visit(self, list_obj):
		if isinstance(list_obj, Stack):
			display_message = "\n-------\n"
			itr = iter(list_obj.list)
			for i in itr:
				display_message += '   '+str(i)+'   '
				display_message += "\n-------\n"
	
		elif isinstance(list_obj, Queue):
			display_message = "\n|"
			itr = iter(list_obj.list)
			for i in itr:
				display_message += str(i) + "|"
			display_message += "\n"
		else:
			display_message = "\n("
			for i in list_obj.list:
				index = list_obj.list.index(i)
				if index < len(list_obj.list) - 1:
					display_message += str(i) + ","
				else:
    					display_message += str(i) + ")\n"
	
		self.log(display_message)
	
	@abc.abstractmethod
	def log(self, display_message):
		raise NotImplementedError('child objects must define log to create a printer')
		
class ScreenPrinter(Printer):
	def __init__(self, *args, **kwargs):
		super(ScreenPrinter, self).__init__(*args, **kwargs)

	def log(self, display_message):
		print(self.name)
		print(display_message)

class FilePrinter(Printer):
	def __init__(self, file_path, *args, **kwargs):
		self.file_path = file_path
		super(FilePrinter, self).__init__(*args, **kwargs)
	
	def log(self, display_message):
		with open(self.file_path, 'a') as f:
			f.write(self.name)
			f.write(display_message)

class Calculator:
    
	@staticmethod
	def union(first_list, second_list):
		if isinstance(first_list,Queue) and isinstance(second_list,Queue):
			merged_queue = Queue(max_size=first_list.max_size+second_list.max_size)
			
			for i in first_list.list:
				merged_queue.append(i)
			
			for i in second_list.list:
				merged_queue.append(i)

			merged_queue.n = first_list.n + second_list.n
			return merged_queue
		elif isinstance(first_list,Stack) and isinstance(second_list,Stack):
			merged_stack = Stack(max_size=first_list.max_size+second_list.max_size)

			for i in second_list.list:
				merged_stack.append(i)

			for i in first_list.list:
				merged_stack.append(i)

			merged_stack.n = first_list.n + second_list.n
			return merged_stack
		elif isinstance(first_list,List) and isinstance(second_list,List):
			merged_list = List()
			first_index = 0
			second_index = 0
			while (first_index < first_list.n) and (second_index < second_list.n):
				if rand.uniform(0,1) < 0.5:
					merged_list.append(first_list.list[first_index])
					first_index = first_index + 1
				else:
					merged_list.append(second_list.list[second_index])
					second_index = second_index + 1
			while first_index < first_list.n:
				merged_list.append(first_list.list[first_index])
				first_index = first_index + 1
			while second_index < second_list.n:
				merged_list.append(second_list.list[second_index])
				second_index = second_index + 1
			return merged_list
		else:
			raise ValueError('The types of both lists are different')