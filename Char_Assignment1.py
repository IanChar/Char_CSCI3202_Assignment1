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
        self.parent = key
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
        if isinstance(parentNode, Node):
            self.parent = parentNode
        else:
            raise TypeError("Parent must be of type Node.")

    def setLeftChild(self, leftChild):
        if isinstance(leftChild, Node):
            self.leftChild = leftChild
        else:
            raise TypeError("Children must be of type Node.")

    def setRightChild(self, rightChild):
        if isinstance(rightChild, Node):
            self.rightChild = rightChild
        else:
            raise TypeError("Children must be of type Node.")

class BinaryTree(object):
    def __init__(self, rootValue):
        self.root = Node(rootValue)
        self.activeNodes = {self.root: True}

    def getRoot(self):
        return self.root
        
    def add(value, parentValue)
        try:


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

testStrucs()
