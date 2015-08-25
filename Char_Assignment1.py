# 1. Queue
from Queue import Queue as BuiltInQueue
class Queue(object):
    def __init__(self):
        self.builtInQueue = BuiltInQueue()

    def push(self, someInteger):
        if isinstance(someInteger, int):
            self.builtInQueue.put(someInteger)
        else:
            raise TypeError("This queue only accepts integers.")

    def pop(self):
        if self.builtInQueue.qsize() == 0:
            raise IndexError("Pop from empty queue.")
        return self.builtInQueue.get()

    def isEmpty(self):
        return self.builtInQueue.empty()

    def size(self):
        return self.builtInQueue.qsize()

# 2. Stack
class Stack(object):
    def __init__(self):
        self.list = []

    def push(self, someInteger):
        if isinstance(someInteger, int):
            self.list.append(someInteger)
        else:
            raise TypeError("This stack only accepts integers.")

    def pop(self):
        if len(self.list) == 0:
            raise IndexError("Pop from empty stack.")
        return self.list.pop()

    def checkSize(self):
        return len(self.list)

# 3. Binary Tree
class Node(object):
    def __init__(self, key, parent = None, leftChild = None, rightChild = None):
        self.key = key
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getKey(self):
        return self.key

    def getParent(self):
        return self.parent

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setKey(self, someInteger):
        if isinstance(someInteger, int):
            self.key = someInteger
        else:
            raise TypeError("Nodes can only have integers for keys.")

    def setParent(self, parentNode):
        if isinstance(parentNode, Node) or parentNode is None:
            self.parent = parentNode
        else:
            raise TypeError("Parent must be of type Node or None.")

    def setLeftChild(self, leftChild):
        if isinstance(leftChild, Node) or leftChild is None:
            self.leftChild = leftChild
        else:
            raise TypeError("Children must be of type Node or None.")

    def setRightChild(self, rightChild):
        if isinstance(rightChild, Node) or rightChild is None:
            self.rightChild = rightChild
        else:
            raise TypeError("Children must be of type Node or None.")

    def __str__(self):
        return str(self.key)

class BinaryTree(object):
    def __init__(self, rootValue):
        self.root = Node(rootValue)
        self.keyNodeMap = {rootValue: [self.root]}

    def getRoot(self):
        return self.root

    # Will try to add to the oldest node with parentValue first.
    # This will add one node to the tree at most.
    def add(self, value, parentValue):
        if not parentValue in self.keyNodeMap:
            print "Parent not found."
            return
        parentList = self.keyNodeMap[parentValue]
        nodeHasBeenAdded = False
        for n in parentList:
            if n.getLeftChild() is None:
                newNode = Node(value, n)
                n.setLeftChild(newNode)
                if not value in self.keyNodeMap:
                    self.keyNodeMap[value] = [newNode]
                else:
                    self.keyNodeMap[value].append(newNode)
                nodeHasBeenAdded = True
                break
            elif n.getRightChild() is None:
                newNode = Node(value, n)
                n.setRightChild(newNode)
                if not value in self.keyNodeMap:
                    self.keyNodeMap[value] = [newNode]
                else:
                    self.keyNodeMap[value].append(newNode)
                nodeHasBeenAdded = True
                break
        if not nodeHasBeenAdded:
            print "Parent(s) has two children, node not added."

    # Will delete all valid nodes with the given value
    def delete(self, value):
        if not value in self.keyNodeMap:
            print "Node not found."
            return
        nodeList = self.keyNodeMap[value]
        for n in nodeList:
            if n.getLeftChild() is None and n.getRightChild() is None:
                parent = n.getParent()
                if parent.getLeftChild() is n:
                    parent.setLeftChild(None)
                else:
                    parent.setRightChild(None)
                nodeList.remove(n)
            else:
                print "Node not deleted, has children."
        if len(nodeList) == 0:
            del self.keyNodeMap[value]

    # Returns a string. Will be called in the context: print <someTreeHere>
    def __str__(self):
        def printCurrNode(currNode):
            if currNode is None:
                return ""
            return (" " + str(currNode) + " "
                    + printCurrNode(currNode.getLeftChild())
                    + printCurrNode(currNode.getRightChild()))
        return printCurrNode(self.root)

# 5. Testing
import random
def testStrucs():
    print "-----------------1 Queue-----------------"
    queue = Queue()
    # Queue 10 random integers
    for _ in range(10):
        randInt = random.randrange(100)
        print "Queueing", randInt
        queue.push(randInt)
    print ""
    # Dequeue the 10 random integers and print them
    for _ in range(10):
        print "Dequeueing", queue.pop()

    print "\n-----------------2 Stack-----------------"
    stack = Stack()
    # Push 10 random integers onto the stack
    for _ in range(10):
        randInt = random.randrange(100)
        stack.push(randInt)
        print "Pushing", randInt, " Current size:", stack.checkSize()
    print ""
    # Pop 10 random integers off the stack
    for _ in range(10):
        print "Popped", stack.pop(), " Current size:", stack.checkSize()

    print "\n-----------------3 Tree-----------------"
    print "Building tree... "
    tree = BinaryTree(0)
    tree.add(1, 0)
    tree.add(2, 0)
    tree.add(3, 1)
    tree.add(4, 1)
    tree.add(5, 2)
    tree.add(6, 2)
    tree.add(7, 3)
    tree.add(8, 3)
    tree.add(9, 4)
    print tree
    print "\nRemoving 6 and 7..."
    tree.delete(6)
    tree.delete(7)
    print tree

if __name__ == "__main__":
    testStrucs()
