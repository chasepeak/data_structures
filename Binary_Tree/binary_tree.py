'''
Chase M. Peak
Binary tree abstract data structure
'''

class TreeNode:
    def __init__(self, key, data, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


    def __repr__(self):
        return str((self.key, self.data))


    def is_leaf(self):
        return self.left == self.right == None


    def __eq__(self, other):
        return self.data == other.data

class BinaryTree:
    def __init__(self):
        self.root = None


    def __repr__(self):
        return str(self.in_order_list())


    def __getitem__(self, i):
        return self.in_order_list()[i]


    def is_empty(self):
        return self.root == None


    def search(self, key):
        if self.is_empty():
            return False
        return self.rec_search(key, self.root)

    def rec_search(self, key, node):
        if node.key == key:
            return True
        elif key > node.key:
            if node.right == None:
                return False
            self.rec_search(key, node.right)
        elif key < node.key:
            if node.left == None:
                return False
            self.rec_search(key, node.left)


    def get_data(self, key):
        if not self.is_empty():
            return self.rec_get_data(key, self.root)

    def rec_get_data(self, key, node):
        if node.key == key:
            return node.data
        elif key > node.key:
            if node.right != None:
                self.rec_get_data(key, node.right)
        elif key < node.key:
            if node.left != None:
                self.rec_get_data(key, node.left)


    def find_min(self):
        if not self.is_empty():
            return self.rec_find_min(self.root)

    def rec_find_min(self, node):
        return node if node.left == None else self.rec_find_min(node.left)


    def find_max(self):
        if not self.is_empty():
            return self.rec_find_max(self.root)

    def rec_find_max(self, node):
        return node if node.right == None else self.rec_find_max(self.right)


    def insert(self, key, data):
        new_node = TreeNode(key, data)
        if not self.root:
            self.root = new_node
        else:
            self.rec_insert(new_node, self.root)

    def rec_insert(self, new_node, node):
        if new_node.key > node.key:
            if node.right == None:
                node.right = new_node
            else:
                self.rec_insert(new_node, node.right)
        elif new_node.key < node.key:
            if node.left == None:
                node.left = new_node
            else:
                self.rec_insert(new_node, node.left)
        node.data = new_node.data #this overwrites the data if a duplicate is inserted


    def delete(self, key): #lazy delete
        self.insert(key, None)


    def in_order_list(self):
        list = []
        if self.is_empty():
            return list
        return self.rec_in_order_list(self.root, list)

    def rec_in_order_list(self, node, list):
        if node != None:
            self.rec_in_order_list(node.left, list)
            list += [node]
            self.rec_in_order_list(node.right, list)
        return list


    def pre_order_list(self):
        list = []
        if self.is_empty():
            return list
        return self.rec_pre_order_list(self.root, list)

    def rec_pre_order_list(self, node, list):
        if node != None:
            list += [node]
            self.rec_pre_order_list(node.left, list)
            self.rec_pre_order_list(node.right, list)
        return list


    def post_order_list(self):
        list = []
        if self.is_empty():
            return list
        return self.rec_post_order_list(self.root, list)

    def rec_post_order_list(self, node, list):
        if node != None:
            self.rec_post_order_list(node.left, list)
            self.rec_post_order_list(node.right, list)
            list += [node]
        return list


    def tree_height(self):
        if not self.is_empty():
            self.rec_tree_height(self.root)

    def rec_tree_height(self, node):
        if node.left != None and node.right != None:
            return 1 + max(self.rec_tree_height(node.left), self.rec_tree_height(node.right))
        elif node.left != None:
            return 1 + self.rec_tree_height(node.left)
        elif node.right != None:
            return 1 + self.rec_tree_height(node.right)
        return 0
