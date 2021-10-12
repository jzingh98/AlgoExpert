# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	branchSums = recurse(root, 0)
    return branchSums

def recurse(node, sumSoFar):
	# Base Case
	if node.left is None and node.right is None:
		return [sumSoFar + node.value]
	
	# Recursive Case
	sums = []
	if node.left:
		left = recurse(node.left, sumSoFar + node.value)
		sums.extend(left)
	if node.right:
		right = recurse(node.right, sumSoFar + node.value)
		sums.extend(right)
	return sums
	
	
