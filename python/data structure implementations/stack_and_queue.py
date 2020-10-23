'''
This is a basic explanation and implementation of Stacks and Queues in Python3.

A stack is a data structure which is similar to a "stack" of books on a table.
The elements in stacks follow a LIFO-Order, which stands for "Last In First Out".

This is similar to placing books on top of each other, making a stack of them.
The top-most book is the one which is removed, making it LIFO.
A basic implementation using lists is shown below.
'''

#Adds elements to the stack
def add_to_stack(stack, element):
	stack.append(element)

#Returns the top-most element if possible, else returns false
def pop_from_stack(stack):
	if(len(stack)>0):
		return(stack.pop())
	else:
		return False

#Demonstrate LIFO Principle
my_stack = []
add_to_stack(my_stack, 'First')
add_to_stack(my_stack, 'Second')
add_to_stack(my_stack, 'Last')

#Notice that the last element is printed first
print(pop_from_stack(my_stack))
print(pop_from_stack(my_stack))
print(pop_from_stack(my_stack))


'''
Queues are very similar to stacks, except that they follow FIFO-Ordering.
FIFO stands for "First In First Out", and this is very intuitive!

Similar to Queues in real life, where we want the first person to join the Queue to be served first
A basic implementation is shown below:
'''

#Add elements to queue
def add_to_queue(queue, element):
	queue.append(element)

#Return the element from the queue, else return false if the queue is empty
def pop_from_queue(queue):
	if(len(queue)>0):
		return(queue.pop(0))
	else:
		return False

#Demonstrate FIFO Principle
my_queue = []
add_to_queue(my_queue, 'First')
add_to_queue(my_queue, 'Second')
add_to_queue(my_queue, 'Last')

#Notice that the Elements are printed in order
print(pop_from_queue(my_queue))
print(pop_from_queue(my_queue))
print(pop_from_queue(my_queue))