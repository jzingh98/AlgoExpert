
def findClosestValueInBst(tree, target):
    # Write your code here.
	winner = traverseTree(tree, target)
	
    return winner


def traverseTree(node, target):
	candidates = []
	
	if node.left:
		candidates.append(traverseTree(node.left, target))
		
	candidates.append(node.value)
		
	if node.right:
		candidates.append(traverseTree(node.right, target))
	
	differences = [abs(x - target) for x in candidates]
	minIndex = differences.index(min(differences))	
	return candidates[minIndex]



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
