# BST: binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree
#       and is smaller than the values in all the nodes in that node's right subtree
# Q: Check if a given binary search tree contains a given value


import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    pass
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))
