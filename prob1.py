class Stack(object):
	def __init__(self, value=None):
		self.stack = []
		if value:
			self.stack.append(value)
		
	def push(self, value):
		self.stack.append(value)

	def peek(self):
		return self.stack[-1]

	def pop(self):
		if self.stack:
			return self.stack.pop()
		return None

	def __str__(self):
		return (str(self.stack))

class Queue(object):
	def __init__(self, value=None):
		self.queue = []
		if value:
			self.queue.append(value)

	def enqueue(self, value):
		self.queue.append(value)

	def dequeue(self):
		if self.queue:
			temp = self.queue[0]
			del self.queue[0]
			return temp
		return None

	def __str__(self):
		return (str(self.queue))

if __name__ == '__main__':
	s = Stack(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)
	q = Queue()
	
	c = 1
	tot = len(s.stack)
	while c < tot:
		while len(s.stack) > c:
			el = s.pop()
			q.enqueue(el)
		while len(q.queue) > 0:
			s.push(q.dequeue)
		c += 1
	print (s)
