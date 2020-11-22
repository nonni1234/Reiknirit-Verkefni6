class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def __int__(self):
        return self.value
    def __str__(self):
        return str(self.value)

    def insert(self, d):
        if d < self.value:
            if self.left == None:
                self.left = Node(d)
            else:
                self.left.insert(d)
        elif d > self.value:
            if self.right == None:
                self.right = Node(d)
            else:
                self.right.insert(d)

    def find(self, d):
        if self.value == d:
            return True
        elif self.left and d <= self.left.value:
            return self.left.find(d)
        elif self.right and d >= self.right.value:
            return self.right.find(d)
        else:
            return False

    def preOrderPrint(self):
        print(self.value)
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()


    def postOrderPrint(self):
        if self.left:
            self.left.postOrderPrint()
        if self.right:
            self.right.postOrderPrint()
        print(self.value)
    def delete(self,root, d):
        if d < self.value: # Left subtree
            self.left = self.left.delete(d)
        elif d > self.value:
            self.right = self.right.delete(d)
        else:

            if not root.left and not root.right:
                root = None
                return root
            elif not root.left:
                

