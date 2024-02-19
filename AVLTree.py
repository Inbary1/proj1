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

	def make_root(self):
		self.parent = None



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

		if not parent.is_real_node():
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

			if node.get_left().get_key() is None:  # only 1 right son
				
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

		while parent is not None:
			
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

	def avl_to_array_rec (self, node, array, i):

		if node and node.is_real_node():
			i = self.avl_to_array_rec(node.get_left(), array, i)
			array[i] = (node.get_key(), node.get_value())
			i += 1
			i = self.avl_to_array_rec(node.get_right(), array, i)
		
		return i

	def avl_to_array(self):

		array = [None] * self.size()
		self.avl_to_array_rec(self.root, array, 0)
		return array
	

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

		x = node 

		left_tree = AVLTree()

		if x.get_left().is_real_node():
			left_tree.root = x.get_left()
			left_tree.get_root().make_root()

		else:
			left_tree.root = None


		right_tree = AVLTree()

		if x.get_right().is_real_node():
			right_tree.root = x.get_right()
			right_tree.get_root().make_root()
		else:
			right_tree.root = None
		

		parent = x.get_parent()

		while parent is not None:

			if parent.get_right() == x: # x is right son

				left_son = AVLTree()
				left_son.root = parent.get_left()
				left_son.get_root().make_root()
				left_tree.join(left_son, parent.get_key(), parent.get_value())

			else: # x is left son

				right_son = AVLTree()
				right_son.root = parent.get_right()
				right_son.get_root().make_root()
				right_tree.join(right_son, parent.get_key(), parent.get_value())

			x = parent
			parent = parent.get_parent()
	
		return [left_tree, right_tree]



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

		if self.get_root() != None and tree2.get_root() != None:

			if self.get_root().get_height() < tree2.get_root().get_height():

				if self.get_root().get_key() < key:
					return AVLTree.join_small_short(self, tree2, key, val)

				else:
					return AVLTree.join_big_short(self, tree2, key, val)

			else:

				if self.get_root().get_key() < key:	
					return AVLTree.join_big_short(tree2, self, key, val)

				else:
					return AVLTree.join_small_short(tree2, self, key, val)
				
		elif self.get_root() == None: # self is empty tree

			h = tree2.get_root().get_height()
			tree2.insert(key, val)
			self.root = tree2.get_root()
			return h+1
		
		else: # tree2 is empty tree
			
			h = self.get_root().get_height()
			self.insert(key, val)
			tree2.root = self.get_root()
			return h+1


	def join_small_short(tree1, tree2, key, val): #tree 1 has smaller values and shorter

		a = tree1.get_root()
		b = tree2.get_root()

		h = b.get_height() - a.get_height()

		x = AVLNode.new_leaf(key, val)

		i = 0

		while i < h and b.get_left().is_real_node():
			b = b.get_left()
			i += 1

		c = b.get_parent()

		x.set_right(b)
		x.set_left(a)

		c.set_left(x)
		x.set_parent(c)
		x.set_height(a.get_height() + 1)
		b.set_parent(x)
		a.set_parent(x)

		parent = c 
		c = 0

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
				c += tree2.rotation(parent)
				parent = old_parent

		tree1.root = tree2.get_root()
		new_size = tree1.size() + tree2.size() +1
		tree1.tree_size = new_size
		tree2.tree_size = new_size
		return h
	

	def join_big_short(tree1, tree2, key, val): #tree 1 has bigger values and shorter

		a = tree1.get_root()
		b = tree2.get_root()

		h = b.get_height() - a.get_height()

		x = AVLNode.new_leaf(key, val)

		i = 0

		while i < h and b.get_right().is_real_node():
			b = b.get_right()
			i += 1

		c = b.get_parent()

		x.set_right(a)
		x.set_left(b)

		c.set_right(x)
		x.set_parent(c)
		x.set_height(a.get_height() + 1)
		b.set_parent(x)
		a.set_parent(x)

		parent = c 
		c = 0

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
				c += tree2.rotation(parent)
				parent = old_parent

		tree1.root = tree2.get_root()
		new_size = tree1.size() + tree2.size() +1
		tree1.tree_size = new_size
		tree2.tree_size = new_size
		return h


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
	print(tree.avl_to_array())

	tree1 = AVLTree()
	tree1.insert(7,7)
	tree1.insert(6,6)
	tree1.insert(10,10)
	tree1.insert(9,9)
	print(tree1.avl_to_array())
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
	print(tree2.avl_to_array())

	pointer = tree2.get_root().get_right().get_right()

	print (tree2.delete(pointer))

	tree3 = AVLTree()
	tree3.insert(30,30)
	tree3.insert(24,24)
	tree3.insert(40,40)
	tree3.insert(26,26)
	tree3.insert(35,35)
	tree3.insert(45,45)
	print(" ")



	print(tree2.join(tree3, 23 ,23))


	tree4 = AVLTree()
	tree4.insert(8,8)
	tree4.insert(4,4)
	tree4.insert(9,9)
	tree4.insert(2,2)
	print(" ")

	tree5 = AVLTree()
	tree5.insert(23,23)
	tree5.insert(15,15)
	tree5.insert(30,30)
	tree5.insert(12,12)
	tree5.insert(20,20)
	tree5.insert(24,24)
	tree5.insert(40,40)
	tree5.insert(13,13)
	tree5.insert(18,18)
	tree5.insert(22,22)
	tree5.insert(25,25)
	tree5.insert(26,26)
	tree5.insert(38,38)
	tree5.insert(42,42)
	tree5.insert(41,41)
	tree5.insert(45,45)

	print(" ")

	node = tree5.get_root().get_right().get_left().get_right()

	list = tree5.split(node)

	tree_left = list[0]
	tree_right = list[1]

	print("test")






testing()
print("test")
