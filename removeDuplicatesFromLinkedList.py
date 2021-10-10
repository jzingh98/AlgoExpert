# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	currentNode = linkedList
	previousNode = None
	while currentNode is not None:
		if previousNode and previousNode.value == currentNode.value:
			previousNode.next = currentNode.next
		else:
			previousNode = currentNode
		currentNode = currentNode.next
	return linkedList
