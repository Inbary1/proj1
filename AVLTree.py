#username - saarmolina

#id1      - 206968216
#name1    - Saar Molina

#id2      - 318672680
#name2    - Inbar Yakov 


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):

		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
				

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):

		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):

		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the bf 

	@rtype: int
	@returns: the bf of self
	"""

	def get_bf(self):
		return (self.get_left().get_height() - self.get_right().get_height())
		

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):

		return self.key is not None
	
	def new_leaf(key, value):

		leaf = AVLNode (key, value)
		virtual1 = AVLNode (None, None)
		virtual2 = AVLNode (None, None)

		leaf.set_right(virtual1)
		leaf.set_left(virtual2)

		virtual1.set_parent(leaf)
		virtual2.set_parent(leaf)

		leaf.set_height(0)

		return leaf

	def is_leaf(self):

		if self.is_real_node():
			return (self.get_right().is_real_node() == False) and (self.get_left().is_real_node() == False)
		
		else:
			return True 

	

	def update_height(self):
		new_height = 1 + max(self.get_left().get_height(), self.get_right().get_height())
		self.set_height(new_height)



"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode(None, None)

		# add your fields here
		self.tree_size = 0 



	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""

	def search(self, key):

		node = self.root
		
		while node.is_real_node():

			if key == node.get_key():
				return node
			
			elif key < node.get_key():
				node = node.get_left()
			
			else:
				node = node.get_right()

		return None
	

	
	def find_parent(self, new_node):

		node = self.root

		parent = node
		
		while node.is_real_node():

			parent = node

			if new_node.get_key() < node.get_key():
				node = node.get_left()
			
			else:
				node = node.get_right()

		return parent
	


	def BST_insert(self, parent, new_node):

		if parent.is_real_node() == False:
			self.root = new_node

		else: 

			new_node.set_parent(parent)

			if new_node.get_key() < parent.get_key():
				parent.set_left(new_node)

			else:
				parent.set_right(new_node)


	
	def right_rotation(self,B):

		A = B.get_left()
		AR = A.get_right()

		A.set_right(B)

		if B.get_parent() != None: 
			A.set_parent(B.get_parent())
			B.get_parent().set_right(A)

		else:  #B is root 
			self.root = A 
			A.set_parent(None)

		B.set_parent(A)
		B.set_left(AR)
		
		B.update_height()
		A.update_height()

		if AR is not None:
			AR.set_parent(B)


	def left_rotation(self, B):

		A = B.get_right()
		AL = A.get_left()

		A.set_left(B)

		if B.get_parent() != None: 
			A.set_parent(B.get_parent())
			B.get_parent().set_left(A)


		else:  #B is root 
			self.root = A 
			A.set_parent(None)

		B.set_parent(A)
		B.set_right(AL)

		B.update_height()
		A.update_height()

		if AL is not None:
			AL.set_parent(B)


	def left_right_rotation(self, C):

		A = C.get_left()
		self.left_rotation(A)
		C.set_left(A.get_parent())
		self.right_rotation(C)

	def right_left_rotation(self, C):

		A = C.get_right()
		self.right_rotation(A)
		C.set_right(A.get_parent())
		self.left_rotation(C)


	def rotation(self, node):

		c = 0

		if node.get_bf() == -2:

			if node.get_right().get_bf() == -1 or node.get_right().get_bf() == 0:
				self.left_rotation(node)
				c += 1

			else:
				self.right_left_rotation(node)
				c += 2


		else:

			if node.get_left().get_bf() == 1 or node.get_left().get_bf() == 0:
				self.right_rotation(node)
				c += 1

			else:
				self.left_right_rotation(node)
				c += 2

		return c

				
	def print_tree(root, level=0, prefix="Root: "):
		if root is not None:
			print(" " * (level * 4) + prefix + str(root.value))
			if root.left is not None or root.right is not None:
				AVLTree.print_tree(root.left, level + 1, "L--- ")
				AVLTree.print_tree(root.right, level + 1, "R--- ")


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def insert(self, key, val):

		c = 0
		new_node = AVLNode.new_leaf(key,val)
		parent = self.find_parent(new_node)

		self.BST_insert(parent, new_node)
		self.tree_size += 1 

		while parent is not None and parent.is_real_node():
			
			old_height = parent.get_height()
			parent.update_height()
			bf = parent.get_bf()

			if abs(bf) < 2:
				
				if old_height == parent.get_height():

					break

				else:

					parent = parent.get_parent()

			else:

				old_parent = parent.get_parent()
				c += self.rotation(parent)
				parent = old_parent
			
		return c
	

	def min(x):

		while x.get_left().is_real_node():
			x = x.get_left()

		return x


	def successor(self, x):

		if x.get_right().is_real_node():
			return min(x.get_right())
		
		y = x.get_parent()

		while y.is_real_node() and x == y.get_right():

			x = y 
			y = x.get_parent()

		return y
		


	def BST_delete(self, parent, node):

		if node.is_real_node and node.is_leaf():
				
			if parent.is_real_node(): # no sons

				if node.get_key() < parent.get_key():
					parent.set_left(AVLNode(None, None))
				
				else:
					parent.set_right(AVLNode(None, None))

			else:

				self.root = AVLNode(None, None)

		else: 

			if node.get_left().get_key() is None:  #only 1 right son
				
				if parent.is_real_node():

					if node.get_key() < parent.get_key(): # node < parent
						parent.set_left(node.get_right())
				
					else: # parent < node
						parent.set_right(node.get_right())

					node.get_right().set_parent(parent)
				
				else:

					self.root = node.get_right()
				
			elif node.get_right().get_key() is None: # only 1 left son
					
				if parent.is_real_node():

					if node.get_key() < parent.get_key(): # node < parent
						parent.set_left(node.get_left())
				
					else: # parent < node
						parent.set_right(node.get_left())

					node.get_left().set_parent(parent)

				else:

					self.root = node.get_left()

			else: # 2 sons

				y = self.successor(node)

				y_parent = y.get_parent()

				if y_parent.get_key() < y.get_key():

					y_parent.set_right(y.get_right())
					y.get_right().set_parent(y_parent)
						
				else:
					y_parent.set_left(y.get_right())
					y.get_right().set_parent(y_parent)

				y.set_right(node.get_right())
				node.get_right().set_parent(y)

				y.set_left(node.get_left())
				node.get_left().set_parent(y)
				
				if parent.is_real_node():

					y.set_parent(parent)

					if node.get_key() < parent.get_key():

						parent.set_left(y)

					else: 
						parent.set_right(y)

				else:

					self.root = y
				


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def delete(self, node):

		c = 0
	
		parent = node.get_parent()
		self.BST_delete(parent, node)
		self.tree_size -= 1 

		while parent is not None and parent.is_real_node():
			
			old_height = parent.get_height()
			parent.update_height()
			bf = parent.get_bf()

			if abs(bf) < 2:
				
				if old_height == parent.get_height():

					break

				else:

					parent = parent.get_parent()

			else:

				old_parent = parent.get_parent()
				c += self.rotation(parent)
				parent = old_parent
			
		return c

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.tree_size	

	
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None

	
	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val):
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
	
	


def testing ():
	tree = AVLTree()
	tree.insert(25, 25)
	tree.insert(9, 9)
	tree.insert(33, 33)
	tree.insert(5,5)
	tree.insert(13,13)
	tree.insert(29,29)
	tree.insert(59,59)
	tree.insert(2,2)
	tree.insert(11,11)
	tree.insert(20,20)
	tree.insert(31,31)
	tree.insert(18, 18)
	tree.insert(23, 23)
	tree.insert(10,10)
	print(tree.insert(24,24))
	tree.insert(50,50)
	print(tree.insert(55,55))

	tree1 = AVLTree()
	tree1.insert(7,7)
	tree1.insert(6,6)
	tree1.insert(10,10)
	tree1.insert(9,9)
	pointer = tree1.get_root().get_left()
	print(tree1.delete(pointer))
	print("test")

	tree2 = AVLTree()
	tree2.insert(15,15)
	tree2.insert(8,8)
	tree2.insert(22,22)
	tree2.insert(4,4)
	tree2.insert(11,11)
	tree2.insert(20,20)
	tree2.insert(24,24)
	tree2.insert(2,2)
	tree2.insert(9,9)
	tree2.insert(12,12)
	tree2.insert(18,18)
	tree2.insert(13,13)

	pointer = tree2.get_root().get_right().get_right()


	print (tree2.delete(pointer))

	print("test")






testing()
print("test")
