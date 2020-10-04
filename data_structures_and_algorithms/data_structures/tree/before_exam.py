class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_ord(self):
      output = []
      def _walk(node):
        if node == None:
          return
        output.append(node.value)
        _walk(node.left)
        _walk(node.right)
      _walk(self.root)
      return output

    def in_ord(self):
      output = []
      def _walk(node):
        if node == None:
          return
        _walk(node.left)
        output.append(node.value)
        _walk(node.right)
      _walk(self.root)
      return output

    def post_ord(self):
      output = []
      def _walk(node):
        if node == None:
          return
        _walk(node.left)
        _walk(node.right)
        output.append(node.value)
      _walk(self.root)
      return output

    def add(self,val):
      curr = self.root
      while curr:
        if curr.value > val:
          if curr.left == None:
            curr.left = Node(val)
            break
          curr = curr.left
        if curr.value < val:
          if curr.right == None:
            curr.right = Node(val)
            break          
          curr = curr.right

    def contain(self,val):
      curr = self.root
      while curr:
        if curr.value == val:
          return True
        elif curr.value > val:
          curr = curr.left
        else:
          curr = curr.right
      return False

def maxx(tree):
  maxx = [tree.root.value]
  def _walk(node):
    if node == None:
      return
    if node.value > maxx[0]:
      maxx[0]=node.value
    _walk(node.left)
    _walk(node.right)
  _walk(tree.root)
  return maxx[0]

def bft(tree):
  res=[]
  temp=[tree.root]
  while temp:
    curr = temp.pop(0)
    if curr.left:
      temp.append(curr.left)
    if curr.right:
      temp.append(curr.right)
    res.append(curr.value)
  return res

def fizz(tree):
  
  def _chick(val):
    if val%5 == 0 and val%3 == 0:
      return 'FizzBuzz'
    elif val%5 == 0:
      return 'Buzz'
    elif val%3 == 0:
      return 'Fizz'
    else:
      return val
  
  def _walk(node):
    if node == None:
      return
    node.value = _chick(node.value)
    _walk(node.left)
    _walk(node.right)
  _walk(tree.root)
  return tree

def sum(tree):
  total = [0]
  def _walk(node):
    if node == None:
      return
    
    total[0] = total[0] + node.value
    _walk(node.left)
    _walk(node.right)
  _walk(tree.root)

  return total[0]

def height(root):

	# Base case: empty  has height 0
	if root is None:
		return 0

	# recur for left and right subtree and consider maximum depth
	return 1 + max(height(root.left), height(root.right))



              


if __name__=='__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(1)
    tree.root.right = Node(1)
    tree.root.right.right = Node(1)
    tree.root.right.left = Node(2)
    # tree.root.left.left = Node(2)
    # tree.root.left.right = Node(20)
    # tree.root.right.right.left = Node(9)
    # tree.root.left.right.left = Node(5)
    # tree.root.left.right.right = Node(11)
    
    print (height(tree.root))