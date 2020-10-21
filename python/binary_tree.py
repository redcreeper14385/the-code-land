'''
This code snippet is to explain how a binary tree is constructed, and one of its implementations in Python3.
We will discussing the basic structure and properties of the binary tree.

A Binary tree is made up of "Nodes". Each node is connected to atmost two other nodes.
We typically draw these two "child" nodes at the bottom of the "parent" node to make the tree simpler to understand.
We usually label the nodes as `left_child` and `right_child`.
The upper node is called as a `parent_node`, and is None if the node in consideration is the top-most node of the tree.
A basic implementation is shown below.
'''

'''
We now define the `add_left_child(x)` method. This method adds x as its left child.
This would require us to change both `left_child` of the present node, and `top_parent` of x.
'''

'''
Similarly, define `add_right_child(x)`
'''

'''
We would now like to print out the tree to see if our structure performs the way we intend it to.
Let the binary tree be represented as root(T1,T2); where T1 is the right subtree and T2 is the left subtree of the root node.
Let  the defined function be `to_string()`

We shall represent root(T1,T2) as "( " + to_string(T1) + " ) " + to_string(T2) 

This seems absurd at first, wouldn't either of the two methods shown below seem more simple and elagant?
	1) "( " + to_string(T1) + " ) " + "( " to_string(T2) + " )"  ----- Parantheses around each
	2) "( " + to_string(T1) + to_string(T2) + " )"  ---- Parantheses around both

However, notice that there is no single unique tree that corresponds to the string "( (  ) )" in case2
Case1 would work, but its just that the number of pairs of parantheses isnt equal to the number of nodes.
It is equal in the representation that we've proposed.
The function implementation is shown below.
'''

class Node:
	def __init__(self):
		self.top_parent = None
		self.left_child = None
		self.right_child = None

	def add_left_child(self, x):
		self.left_child = x
		x.top_parent = self

	def add_right_child(self, x):
		self.right_child = x
		x.top_parent = self

	def print_tree(self):
		s = "( "
		if self.left_child is not None:
			s = s + self.left_child.print_tree() 
		s = s + " )"
		if self.right_child is not None:
			s = s + self.right_child.print_tree()
		return s


#Driver code to check implementation

root = Node()
left = Node()
right = Node()
root.add_left_child(left)
root.add_right_child(right)

s = root.print_tree()
print(s)