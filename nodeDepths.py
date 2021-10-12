def nodeDepths(root):
    # Write your code here.
	sum = recurse(root, 0)
	return sum


def recurse(node, current):
	subSum = current
	if node.left:
		leftSum = recurse(node.left, current + 1)
		subSum += leftSum
	if node.right:
		rightSum = recurse(node.right, current + 1)
		subSum += rightSum
	return subSum
	

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
