from Node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.data = None

    def insert(self, d):
        if self.root == None:
            self.root = Node(d)
        else:
            self.root.insert(d)

    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return False

    def preOrderPrint(self):
        if self.root:
            self.root.preOrderPrint()
        else:
            print("Tré er tómt")

    def postOrderPrint(self):
        if self.root:
            self.root.postOrderPrint()
        else:
            print("Tré er tómt")

    def delete(self, d):
        if self.find(d):
            self.root.delete(self,d)
        else:
            return None