#Purpose :  A perfect binary tree

#Written by Kenny Ng Wai Yu
#On 17/4/2024
#For Assignment 4

from binarytree import Node, bst

# Part (i)
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(root)

# Part (ii)
perfect_bst = bst(height=3, is_perfect=True)
print(perfect_bst)

# Part (iii)
# 1. Print the total number of nodes
num_nodes = len(perfect_bst)
print("Total number of nodes:", num_nodes)

# 2. Print the total number of leaves
num_leaves = len(perfect_bst.leaves)
print("Total number of leaves:", num_leaves)


# 3. Print the left most node in the tree
def left_most_node(node):
    while node.left is not None:
        node = node.left
    return node


print("Left most node in the tree:", left_most_node(perfect_bst))


# 4. Print the right most node in the tree
def right_most_node(node):
    while node.right is not None:
        node = node.right
    return node


print("Right most node in the tree:", right_most_node(perfect_bst))