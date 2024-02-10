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
		if self.is_real_node():
			return self.left
		return None


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		if self.is_real_node():
			return self.right
		return None


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
		return (self.get_right().is_real_node() == False) and (self.get_left().is_real_node() == False)
	

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
		
		while node is not None and node.is_real_node():

			if key == node.get_key():
				return node
			
			elif key < node.get_key():
				node = node.get_left()
			
			else:
				node = node.get_right()

		return None
	

	
	def find_parent(self, new_node):

		node = self.root

		y = node
		
		while node.is_real_node():

			y = node

			if new_node.get_key() < node.get_key():
				node = node.get_left()
			
			else:
				node = node.get_right()

		return y
	


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

		else:  #B is root 
			self.root = A 
			A.set_parent(None)

		B.set_parent(A)
		B.set_left(AR)

		if AR is not None:
			AR.set_parent(B)


	def left_rotation(self, B):

		A = B.get_right()
		AL = A.get_left()

		A.set_left(B)

		if B.get_parent() != None: 
			A.set_parent(B.get_parent())

		else:  #B is root 
			self.root = A 
			A.set_parent(None)

		B.set_parent(A)
		B.set_right(AL)

		if AL is not None:
			AL.set_parent(B)


	def left_right_rotation(self, C):

		A = C.get_left()
		self.left_rotation(A)
		self.right_rotation(C)

	def right_left_rotation(self, C):

		A = C.get_right()
		self.right_rotation(A)
		self.left_rotation(C)


	def rotation(self, node):

		if node.get_bf() == -2:

			if node.get_right().get_bf() == -1:
				self.left_rotation(node)

			else:
				self.right_left_rotation(node)
		
		else:

			if node.get_left().get_bf() == 1:
				self.right_rotation(node)

			else:
				self.left_right_rotation(node)
				
				
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

		new_node = AVLNode.new_leaf(key,val)
		print("new Node: ", key)
		parent = self.find_parent(new_node)
		print("parent: ", parent.key)



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
				self.rotation(parent)
				parent = old_parent



			




	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1


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
	















AVLNode.__repr__ = lambda self: str(self.get_key())

class tests:
    # These functions do the actual testing
    @staticmethod
    def testInsertDelete():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]
        
        # test RL rotation
        testHelper.insert_array(tree, keys[0:5])
        testHelper.assert_neighbors(tree, 7, 4, 11, 5)

        # test LR rotation
        testHelper.insert_array(tree, keys[5:6]) # insert 15
        testHelper.assert_neighbors(tree, 15, None, None, 6)
        testHelper.assert_neighbors(tree, 23, 15, 30, 6)
        testHelper.assert_neighbors(tree, 11, 7, 23, 6)
        testHelper.assert_neighbors(tree, 7, 4, None,6)
        testHelper.test_root(tree, 11)
        
        # test L rotation
        testHelper.insert_array(tree, keys[6:8]) # insert 40, 43
        testHelper.assert_neighbors(tree, 40, 30, 43,8)
        testHelper.assert_neighbors(tree, 23, 15, 40,8)
        
        # testHelper R rotation
        testHelper.insert_array(tree, keys[8:10]) # insert 2, 1
        testHelper.assert_neighbors(tree, 4, 2, 7,10)
        testHelper.assert_neighbors(tree, 2, 1, None,10)
        testHelper.assert_neighbors(tree, 7, None, None,10)
        testHelper.assert_neighbors(tree, 11, 4, 23,10)
        testHelper.test_root(tree, 11)
        
        # test deletions
        testHelper.test_deletion(tree, 1, 0)
        testHelper.assert_neighbors(tree, 4, 2, 7,9)
        testHelper.assert_neighbors(tree, 2, None, None,9)
        testHelper.assert_neighbors(tree, 7, None, None,9)
        testHelper.assert_neighbors(tree, 11, 4, 23,9)
        testHelper.test_root(tree, 11)
        
        testHelper.test_deletion(tree, 2, 0)
        testHelper.assert_neighbors(tree, 4, None, 7,8)
        testHelper.assert_neighbors(tree, 7, None, None,8)
        testHelper.assert_neighbors(tree, 11, 4, 23,8)
        testHelper.test_root(tree, 11)
        
        # test L rotation
        testHelper.test_deletion(tree, 7, 1)
        testHelper.assert_neighbors(tree, 11, 4, 15,7)
        testHelper.assert_neighbors(tree, 23, 11, 40,7)
        testHelper.test_root(tree, 23)
        
        # TODO: empty the tree and test to see everything is correct
        
    @staticmethod
    def test_avl_to_array():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]
        testHelper.insert_array(tree, keys)

        testHelper.test_avl2array(tree, keys)

class testHelper:
    # Helper functions for tests class. No need to use any of them.
    @staticmethod
    def assert_neighbors(tree, node_key, left_key, right_key, size):
        node = tree.search(node_key)
        right_result = tree.search(right_key) if right_key != None else None
        left_result = tree.search(left_key) if left_key != None else None
        node_right = node.get_right() if node != None else None
        node_left = node.get_left() if node != None else None

        assert node_right is right_result, \
            f"Checking neighbors for {node_key}, right neighbor is {node.get_right()} but search returned something else when searching for key {right_key}"
        assert node_left is left_result, \
            f"Checking neighbors for {node_key}, left neighbor is {node.get_left()} but search returned something else when searching for key {left_key}"
        assert tree.size()==size, \
            f"size error"
        
    @staticmethod
    def insert_array(tree, key_array):
        for key in key_array:
            tree.insert(key, key)
            
    @staticmethod
    def test_deletion(tree, deletion_key, num_balancing_actions):
        deletion_node = tree.search(deletion_key)
        check_balacing_actions = tree.delete(deletion_node)

        assert tree.search(deletion_key) is None, \
            f"Deleting {deletion_key}, searching for deleted key did not return None"
        assert check_balacing_actions == num_balancing_actions, \
            f"Deleting {deletion_key}, deletion returned {check_balacing_actions} balancing actions instead of {num_balancing_actions}"
    
    @staticmethod
    def test_root(tree, root_key):
        assert tree.get_root() is tree.search(root_key), \
            f"Root is {tree.get_root()}, but search returned something else when searching for {root_key}"    
    
    """
    @param tree: tree to test
    @param tree_keys_array: Array with all keys present in the tree
    """
    @staticmethod
    def test_avl2array(tree, tree_keys_array):

        expectedArray = [(key, key) for key in sorted(tree_keys_array)] # tests.insert_array uses the key as a value, so we do the same here
        avl_to_array_result = tree.avl_to_array()

        assert expectedArray == avl_to_array_result, \
            f"Expected avl_to_array() to return \n{expectedArray}\nbut got\n{avl_to_array_result}"
		
tests.testInsertDelete()