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
	

	"""Creates a new leaf node for an AVL tree.

    @type key: int or None
    @param key: The key of the new leaf node.
    @type value: any
    @param value: The value associated with the key.

    @rtype: AVLNode
    @returns: A new leaf node with the specified key, value, and virtual children.
    """

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
	

	"""Checks if the current node is a leaf in the AVL tree.

    @rtype: bool
    @returns: True if the node is a leaf, False otherwise.
    """

	def is_leaf(self):

		if self.is_real_node():
			return (self.get_right().is_real_node() == False) and (self.get_left().is_real_node() == False)
		
		else:
			return True 
		

	"""Updates the height of the current node based on the heights of its left and right children.

    @rtype: None
    """

	def update_height(self):
		new_height = 1 + max(self.get_left().get_height(), self.get_right().get_height())
		self.set_height(new_height)


	"""Sets the parent of the current node to None, making it the root of the subtree.

    @rtype: None
    """

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
		
		# Start the search from the root of the AVL tree
		node = self.root
    
    	# Continue searching until a real node is reached
		while node.is_real_node():

        	# Check if the current node's key matches the target key
			if key == node.get_key():
				return node

        	# If the target key is less than the current node's key, move to the left child
			elif key < node.get_key():
				node = node.get_left()

        	# If the target key is greater than the current node's key, move to the right child	
			else:
				node = node.get_right()

    	# If the key is not found, return None 
		return None
	

	"""Finds the parent node where a new node should be inserted in the AVL tree.

    @type new_node: AVLNode
    @param new_node: The new node that needs a parent.

    @rtype: AVLNode
    @returns: The parent node where the new node should be inserted.
    """
	
	def find_parent(self, new_node):

		node = self.root

		parent = node
		
		while node.is_real_node():

			# Update the parent to the current node
			parent = node

			# If the key of the new node is less than the current node's key, move to the left child
			if new_node.get_key() < node.get_key():
				node = node.get_left()
			
			# If the key of the new node is greater than or equal to the current node's key, move to the right child
			else:
				node = node.get_right()

    	# Return the parent node where the new node should be inserted
		return parent
	

	"""Inserts a new node into the AVL tree following the rules of a Binary Search Tree (BST).

    @type parent: AVLNode
    @param parent: The parent node where the new node should be inserted.
    @type new_node: AVLNode
    @param new_node: The new node to be inserted.

    @rtype: None
    """

	def BST_insert(self, parent, new_node):

    	# If the parent is not a real node, set the new node as the root of the AVL tree
		if not parent.is_real_node():
			self.root = new_node
			new_node.make_root()

		else: 
			
			# Set the parent of the new node to be the specified parent
			new_node.set_parent(parent)

        	# If the key of the new node is less than the parent's key, set it as the left child
			if new_node.get_key() < parent.get_key():
				parent.set_left(new_node)

        	# If the key of the new node is greater than or equal to the parent's key, set it as the right child
			else:
				parent.set_right(new_node)


	"""Performs a right rotation in the AVL tree with the given node B as the pivot.

    @type B: AVLNode
    @param B: The pivot node for the right rotation.

    @rtype: None
    """

	def right_rotation(self,B):

		# Get the left child of B (A) and its right child (AR)
		A = B.get_left()
		AR = A.get_right()

		# Set A as the right child of B
		A.set_right(B)

		 # Adjust the parent pointers
		if B.get_parent() != None: 
			A.set_parent(B.get_parent())
			B.get_parent().set_right(A)

		else:  # B is the root, set A as the new root 
			self.root = A 
			A.make_root()

    	# Set B as the left child of A and update the parent pointers
		B.set_parent(A)
		B.set_left(AR)

		# Update the parent pointer of AR
		AR.set_parent(B)
		
		# Update the heights of B and A
		B.update_height()
		A.update_height()

	
	"""Performs a left rotation in the AVL tree with the given node B as the pivot.

    @type B: AVLNode
    @param B: The pivot node for the left rotation.

    @rtype: None
    """

	def left_rotation(self, B):

		# Get the right child of B (A) and its left child (AL)
		A = B.get_right()
		AL = A.get_left()

		# Set A as the left child of B
		A.set_left(B)

		# Adjust the parent pointers
		if B.get_parent() != None: 
			A.set_parent(B.get_parent())
			B.get_parent().set_left(A)


		else:   # B is the root, set A as the new root
			self.root = A 
			A.make_root()

		# Set B as the right child of A and update the parent pointers
		B.set_parent(A)
		B.set_right(AL)

		# Update the parent pointer of AL
		AL.set_parent(B)

		# Update the heights of B and A
		B.update_height()
		A.update_height()
			

	"""Performs a left-right rotation in the AVL tree with the given node C as the pivot.

    @type C: AVLNode
    @param C: The pivot node for the left-right rotation.

    @rtype: None
    """

	def left_right_rotation(self, C):

		# Get the left child of C (A)
		A = C.get_left()

		# Perform a left rotation with A as the pivot
		self.left_rotation(A)

		# Set the left child of C to be the parent of A
		C.set_left(A.get_parent())

		# Perform a right rotation with C as the pivot
		self.right_rotation(C)


	"""Performs a right-left rotation in the AVL tree with the given node C as the pivot.

    @type C: AVLNode
    @param C: The pivot node for the right-left rotation.

    @rtype: None
    """

	def right_left_rotation(self, C):

		# Get the right child of C (A)
		A = C.get_right()

		# Perform a right rotation with A as the pivot
		self.right_rotation(A)

		# Set the right child of C to be the parent of A
		C.set_right(A.get_parent())

		# Perform a left rotation with C as the pivot
		self.left_rotation(C)


	"""Performs a rotation in the AVL tree based on the balance factors of the given node.

    @type node: AVLNode
    @param node: The node for which rotation is performed.

    @rtype: int
    @returns: The number of rotations performed (c).

    """

	def rotation(self, node):

		c = 0

		# Check the balance factor of the given node

		if node.get_bf() == -2: # Left subtree is heavy

			if node.get_right().get_bf() == -1 or node.get_right().get_bf() == 0:

				# Perform a left rotation
				self.left_rotation(node)
				c += 1

			else:

				# Perform a right-left rotation
				self.right_left_rotation(node)
				c += 2

		else: # Right subtree is heavy

			if node.get_left().get_bf() == 1 or node.get_left().get_bf() == 0:

				# Perform a right rotation
				self.right_rotation(node)
				c += 1

			else:

				# Perform a left-right rotation
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

		# Creates a new AVL Node
		new_node = AVLNode.new_leaf(key,val)

		# Finds the parent node where a new node should be inserted 
		parent = self.find_parent(new_node)

		# Perform Binary Search Tree (BST) insertion
		self.BST_insert(parent, new_node)
		self.tree_size += 1 

		# Check and perform rotations to maintain AVL property
		while parent is not None and parent.is_real_node():
			
			# Update height and balance factor of ancestors
			old_height = parent.get_height()
			parent.update_height()
			bf = parent.get_bf()

			if abs(bf) < 2: # If the balance factor is within the acceptable range
		
				if old_height == parent.get_height():  # If the height hasn't changed, no further updates are needed

					break

				else: # Move to the parent for further updates

					parent = parent.get_parent()
					c +=1

			else: # If the balance factor is not within the acceptable range, perform rotations

				old_parent = parent.get_parent()

				c += self.rotation(parent)  # Perform rotations and update rotation counter

				parent = old_parent  # Update parent to its parent before the rotation
			
		return c
	

	"""Finds the minimum key node in the subtree rooted at the given node.

    @type x: AVLNode
    @param x: The starting node for finding the minimum key.

    @rtype: AVLNode
    @returns: The node with the smallest key in the subtree rooted at node x.
	"""

	def min(x):

		while x.get_left().is_real_node():
			x = x.get_left()

		return x


	"""Finds the successor node of the given node x in the AVL tree.

    @type x: AVLNode
    @param x: The node for which the successor is to be found.

    @rtype: AVLNode or None
    @returns: The node that follows x in an in-order traversal, or None if x is the maximum node.
    """

	def successor(self, x):

		if x.get_right().is_real_node():
			return min(x.get_right())
		
		y = x.get_parent()

		while y.is_real_node() and x == y.get_right():

			x = y 
			y = x.get_parent()

		return y
		

	"""Deletes the given node from the AVL tree.

    @type parent: AVLNode
    @param parent: The parent of the node to be deleted.
    
    @type node: AVLNode
    @param node: The node to be deleted from the AVL tree.

    @rtype: None
    @returns: Modifies the AVL tree by removing the specified node and adjusting its parent accordingly.
    """

	def BST_delete(self, parent, node):

		# Case 1: Node is a leaf (has no children)
		if node.is_real_node and node.is_leaf():
				
			if parent.is_real_node(): # Check if the node has a parent

				 # Remove the node as a child of its parent

				if node == parent.get_left():
					parent.set_left(AVLNode(None, None))
				
				else:
					parent.set_right(AVLNode(None, None))

			else:  # Node is the root; set the root to a new empty node

				self.root = AVLNode(None, None)

		# Case 2: Node has only a right child
		elif node.get_left().get_key() is None:  
				
			if parent.is_real_node(): # Check if the node has a parent

				if node == parent.get_left(): # Check if the node is left son
					parent.set_left(node.get_right())
				
				else: # Check if the node is right son
					parent.set_right(node.get_right())

				# Update the parent of the right child
				node.get_right().set_parent(parent)
				
			else:   # Node is the root; set the root to the right child of the node

				self.root = node.get_right()
				node.get_right().make_root()
	
		# Case 3: Node has only a left child
		elif node.get_right().get_key() is None: 
					
			if parent.is_real_node(): # Check if the node has a parent

				if node == parent.get_left(): # Check if the node is left son
					parent.set_left(node.get_left())
				
				else: # Check if the node is right son
					parent.set_right(node.get_left())

				# Update the parent of the left child
				node.get_left().set_parent(parent)

			else: # Node is the root; set the root to the left child of the node

				self.root = node.get_left()
				node.get_left().make_root()

		# Case 4: Node has two children
		else: 

			y = self.successor(node) # Find the successor
			y_parent = y.get_parent()

			# Update the parent of the successor's right child, y can't have left child

			if y == y_parent.get_right(): # Checks if y is right son

				y_parent.set_right(y.get_right()) 
				y.get_right().set_parent(y_parent)
						
			else: # Checks if y is left son

				y_parent.set_left(y.get_right())
				y.get_right().set_parent(y_parent)

			# Set the successor's children to be the node's children
				
			y.set_right(node.get_right())
			node.get_right().set_parent(y)

			y.set_left(node.get_left())
			node.get_left().set_parent(y)

			if parent.is_real_node(): # If the node has a parent, update the parent to point to the successor

				y.set_parent(parent)

				if node == parent.get_left(): # Checks if node is left son

					parent.set_left(y)

				else: # Checks if node is right son
					parent.set_right(y)

			else:  # Node is the root; set the root to the successor

				self.root = y
				y.make_root()


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def delete(self, node):

		c = 0
	
		parent = node.get_parent() # Finds the parent of node

		# Perform Binary Search Tree (BST) deletion
		self.BST_delete(parent, node) 

		self.tree_size -= 1 

		while parent is not None:
			
			# Update height and balance factor of ancestors
			old_height = parent.get_height()
			parent.update_height()
			bf = parent.get_bf()

			if abs(bf) < 2: # If the balance factor is within the acceptable range
				
				if old_height == parent.get_height(): # If the height hasn't changed, no further updates are needed
					
					break

				else: # Move to the parent for further updates

					c += 1
					parent = parent.get_parent()

			else: # If the balance factor is not within the acceptable range, perform rotations

				old_parent = parent.get_parent()
				c += self.rotation(parent) # Perform rotations and update rotation counter
				parent = old_parent # Move to the parent for further updates
			
		return c
	

	"""Recursively converts the AVL tree to an array.

    @param node: The current node being processed.
    @type node: AVLNode

    @param array: The array to store the key-value pairs.
    @type array: list

    @param i: The index to insert the current key-value pair in the array.
    @type i: int

    @return: The updated index for the next insertion in the array.
    @rtype: int
    """
	
	def avl_to_array_rec (self, node, array, i):

		if node and node.is_real_node():

			# Traverse left subtree
			i = self.avl_to_array_rec(node.get_left(), array, i)

			# Insert current node's key-value pair into the array
			array[i] = (node.get_key(), node.get_value())
			i += 1

			# Traverse right subtree
			i = self.avl_to_array_rec(node.get_right(), array, i)
		
		return i

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

	def avl_to_array(self):

		# Create an empty array to store key-value pairs.
		array = [None] * self.size() 

		# Recursively populate the array with key-value pairs.
		self.avl_to_array_rec(self.root, array, 0)

		# Return the sorted array representing the AVL tree.
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

    	# Initialize AVL trees to store left and right subtrees.
		left_tree = AVLTree()
		right_tree = AVLTree()

		# Populate left_tree with the left subtree of the given node.
		if x.get_left().is_real_node():
			left_tree.root = x.get_left()
			left_tree.get_root().make_root()

		else: # Left subtree of the given node is empty
			left_tree.root = None

		# Populate right_tree with the right subtree of the given node.
		if x.get_right().is_real_node():
			right_tree.root = x.get_right()
			right_tree.get_root().make_root()

		else: # Right subtree of the given node is empty
			right_tree.root = None
		
		# Traverse up the tree to split and reconstruct the trees.
		parent = x.get_parent()

		while parent is not None:

			if parent.get_right() == x: # x is right son

				# Create a new left subtree with the current left_tree and parent's left subtree.

				left_son = AVLTree()
				left_son.root = parent.get_left()
				left_son.get_root().make_root()
				left_tree.join(left_son, parent.get_key(), parent.get_value())

			else: # x is left son

				# Create a new right subtree with the current right_tree and parent's right subtree.

				right_son = AVLTree()
				right_son.root = parent.get_right()
				right_son.get_root().make_root()
				right_tree.join(right_son, parent.get_key(), parent.get_value())

			x = parent
			parent = parent.get_parent()
	
		# Return the resulting left_tree and right_tree.
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

		if self.get_root() != None and tree2.get_root() != None: # Both trees are not empty

			# self has smaller height
			if self.get_root().get_height() < tree2.get_root().get_height(): 

				# self conatins the smaller keys
				if self.get_root().get_key() < key: 
					return AVLTree.join_small_short(self, tree2, key, val)

				# self conatins the bigger keys
				else:
					return AVLTree.join_big_short(self, tree2, key, val)

			# self has greater height
			else: 

				# self conatins the smaller keys
				if self.get_root().get_key() < key:	
					return AVLTree.join_big_short(tree2, self, key, val)

				# self conatins the bigger keys
				else:
					return AVLTree.join_small_short(tree2, self, key, val)
				
		elif self.get_root() == None: # self is empty tree

			# Adds the new node to tree2

			h = tree2.get_root().get_height()
			tree2.insert(key, val)
			self.root = tree2.get_root()
			return h+1
		
		else: # tree2 is empty tree

			# Adds the new node to self
			
			h = self.get_root().get_height()
			self.insert(key, val)
			tree2.root = self.get_root()
			return h+1


	"""Joins two AVL trees when tree1 has smaller values and is shorter.

    @param tree1: The AVL tree with smaller values and shorter height.
    @type tree1: AVLTree

    @param tree2: The other AVL tree to be joined.
    @type tree2: AVLTree

    @param key: The key to be inserted into the resulting AVL tree.
    @type key: Any

    @param val: The value to be associated with the key in the resulting AVL tree.
    @type val: Any

    @return: The height difference between the two trees after the join operation.
    @rtype: int
    """

	def join_small_short(tree1, tree2, key, val):

		a = tree1.get_root()
		b = tree2.get_root()

		h = b.get_height() - a.get_height()

		# Creates new node
		x = AVLNode.new_leaf(key, val)

		i = 0

		# Move to the leftmost node of tree2 at the level of height difference
		while i < h and b.get_left().is_real_node():
			b = b.get_left()
			i += 1

		c = b.get_parent()

	 	#Set the children of the new node x
		x.set_right(b)
		x.set_left(a)

		# Update the left child of the parent of b to x
		c.set_left(x)

		# Set the parent of x
		x.set_parent(c)

		# Set the height of x
		x.set_height(a.get_height() + 1)

		# Update the parent pointers of b and a to x
		b.set_parent(x)
		a.set_parent(x)

		parent = c 
		c = 0

		# Update heights and perform rotations until reaching the root
		while parent is not None and parent.is_real_node():
			
			# Update height and balance factor of ancestors
			old_height = parent.get_height()
			parent.update_height()
			bf = parent.get_bf()

			if abs(bf) < 2: # If the balance factor is within the acceptable range
				
				if old_height == parent.get_height(): # If the height hasn't changed, no further updates are needed

					break

				else: # Move to the parent for further updates

					parent = parent.get_parent()

			else: # If the balance factor is not within the acceptable range, perform rotations

				old_parent = parent.get_parent()
				c += tree2.rotation(parent)  # Perform rotations and update rotation counter
				parent = old_parent # Move to the parent for further updates

		# Set the root of tree1 to the root of tree2
		tree1.root = tree2.get_root()

		# Update the size of the trees
		new_size = tree1.size() + tree2.size() +1
		tree1.tree_size = new_size
		tree2.tree_size = new_size

		return h
	

	"""Joins two AVL trees when tree1 has larger values and is shorter.

    @param tree1: The AVL tree with larger values and shorter height.
    @type tree1: AVLTree

    @param tree2: The other AVL tree to be joined.
    @type tree2: AVLTree

    @param key: The key to be inserted into the resulting AVL tree.
    @type key: Any

    @param val: The value to be associated with the key in the resulting AVL tree.
    @type val: Any

    @return: The height difference between the two trees after the join operation.
    @rtype: int
    """

	def join_big_short(tree1, tree2, key, val): 

		a = tree1.get_root()
		b = tree2.get_root()

		h = b.get_height() - a.get_height()

		# Creates new node
		x = AVLNode.new_leaf(key, val)

		i = 0

		# Move to the rightmost node of tree2 at the level of height difference
		while i < h and b.get_right().is_real_node():
			b = b.get_right()
			i += 1

		c = b.get_parent()

		# Set the right child of the new node x
		x.set_right(a)

		# Set the left child of the new node x
		x.set_left(b)

		# Update the right child of the parent of b to x
		c.set_right(x)

		# Set the parent of x
		x.set_parent(c)

		# Set the height of x
		x.set_height(a.get_height() + 1)

		# Update the parent pointers of b and a to x
		b.set_parent(x)
		a.set_parent(x)

		parent = c 
		c = 0

		# Update heights and perform rotations until reaching the root
		while parent is not None and parent.is_real_node():

			# Update height and balance factor of ancestors
			old_height = parent.get_height()
			parent.update_height()
			bf = parent.get_bf()

			if abs(bf) < 2: # If the balance factor is within the acceptable range
				
				if old_height == parent.get_height(): # If the height hasn't changed, no further updates are needed

					break

				else: # Move to the parent for further updates

					parent = parent.get_parent()

			else: # If the balance factor is not within the acceptable range, perform rotations

				old_parent = parent.get_parent()
				c += tree2.rotation(parent) # Perform rotations and update rotation counter
				parent = old_parent # Move to the parent for further updates

		# Set the root of tree1 to the root of tree2
		tree1.root = tree2.get_root()

		# Update the size of the trees
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
