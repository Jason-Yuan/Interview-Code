##############################################################################################################################
#      Project:                  Binary Search Tree
###############################################################################################################################

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def search(node, data):
    if node is None: return None  # data not found
    if data < node.data: return search(node.l_child, data)
    elif data > node.data: return search(node.r_child, data)
    else: return node.data  # found data 

##############################################################################################################################

	