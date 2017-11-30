# • Create your call class with an init method. Each instance of Call() should have:
# Attributes:

# • unique id

# • caller name

# • caller phone number

# • time of call

# • reason for call
# Methods:

# • display: that prints all Call attributes.
import datetime
class Call(object):
	call_id=1
	def __init__(self, name, num, reason, *witnesses):
		call_id = 1
		for person in witnesses:
			print (person)
		self.name= name
		self.call_id = call_id
		Call.call_id +=1
		self.num = num
		self.reason = reason
		self.time = datetime.datetime.now()
	def display(self):
		print ("Call: " + str(self.call_id))
		print ("Caller: " + self.name)
		print ("Phone Num: " + self.num)
		print ("Reason: " + self.reason)
		print ("Time: " + str(self.time))
class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)
	def add(self, new_call):
		self.calls.append(new_call)
		self.queue_size = len(self.calls)
	def remove(self):
		self.call.pop(0)
		self.queue_size = len(self.calls)
	def info(self):
		for call in self.calls:
			print (call.name)
			print (call.num)
			call.display()
	def remove_num(self, num):
		for i in range(0,self.queue_size):
			if call.num == num:
				idx_to_pop = i
			self.calls.pop(idx_to_pop)
			print("removed num!")
	def reorder(self):
		swapped = False
		for i in range(0,self.queue_size):
			if self.calls[i].time > self.calls[i+1].time:
				swapped = True
				temp = self.calls[i]
				self.calls[i] = self.calls[i+1]
				self.calls[i+1] = temp
				self.reorder()
			if not swapped:
				self.info()
	def all_display(self):
		for call in self.calls:
			call.display()


my_call = Call("Frodo", "(123)456-789", "Lost my ring")
my_call.display()
# my_call2 = Call("Gandalf","(123)452-6545","I'm a wizard")

