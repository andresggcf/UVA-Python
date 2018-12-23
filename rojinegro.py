class rbnode(object):
	def __init__ (self, key-None):
		self.k = key
		self.l = self.r = self.p = None 
		self.red = False

	def __str__(self):
		return str(self.k)

class rbtree(object):
	NIL = rbnode()

	def __init__(self):
		self.__root = rbtree.NIL

	def is_empty(self):
		return self.__root == rbtree.NIL

	def minimum (self):
		assert not (self.is_empty())
		ans = self.__root
		while ans.l != rbtree.NIL:
			ans = ans.l
		return ans.k

	def maximum (self):
		assert not (self.is_empty())
		ans = self.__root == rbtree.NIL
		while ans.r != rbtree.NIL:
			ans = ans.r
		return ans.k

	def __left_rotate(self, x):
		y=x.r
		x.r = y.l
		if y.l != rbtree.NIL:
			y.l.p = x
		y.p = x.p
		if x.p == rbtree.NIL:
			self.__root = y
		elif x == x.p.l:
			x.p.l = y
		else: x.p.r = y
		y.l = x
		x.p = y

	def __right_rotate(self,y):
		x = y.l
		y.l = x.r
		if x.r != rbtree.NIL:
			x.r.p = y
		x.p = y.p
		if y.p == rbtree.NIL:
			self.__root = x
		elif y = y.p.l:
			y.p.l = x
		else: y.p.l = x
		x.r = y
		y.p = x