from Tree import Tree
t = Tree()
t.insert(20)
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)
t.preOrderPrint()
print()
#t.delete(20)
t.postOrderPrint()
print()
print(t.find(1))
print(t.find(35))
