'''
Binary Search Tree (BST)

Linear BST: O(n) time
Average BST: O(log n) time

For any particular node:
- The node's left child is less than the node
- The node's right child is greater than the node
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
    def insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
    
    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
    
    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.data
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        
        return helper(self.root)