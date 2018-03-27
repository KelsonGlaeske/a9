# CMPT 145: Primitive Binary Search Trees
# Defines functions for primitive Binary Search Tree data structure
#
# A Primitive Binary Tree is defined as follows:
# 1. The value None is a primitive binary tree;
#    None is an empty tree.
# 2. If lt and rt are primitive binary trees, and d is any value
#    TreeNode(d, lt, rt) is a primitive binary tree.

# A Primitive Binary Tree t satisfies the Binary Search Tree (BST)
# property if all of the following hold:
# 1. The data value stored at TreeNode t is greater than any data
#    value in t's left subtree (if any)
# 2. The data value stored at TreeNode t is less than any data
#    value in t's right subtree (if any)
# 3. t's left subtree satisfies the BST property
# 4. t's right subtree satisfies the BST property


import TreeNode as TN

def member_prim(tnode, target):
    """
    Purpose:
        Check if value is stored in the binary search tree.
    Preconditions:
        :param tnode: a binary search tree
        :param target: a value
    Postconditions:
        none
    :return: True if value is in the tree
    """
    if tnode is None:
        return False
    elif tnode.data is target:
            return True
    elif target < tnode.data:
        return member_prim(tnode.left, target)
    else:
        return member_prim(tnode.right, target)



def insert_prim(tnode, value):
    """
    Insert a new value into the binary search tree.
    Preconditions:
        :param tnode: a TreeNode with the BST property
        :param value: a value
    Postconditions:
        If the value is not already in the tree, it is added
    Return
        :return: tuple (flag, tree)
        flag is True if insertion succeeded;
                tree contains the new value
        flag is False if the value is already in the tree,
                tree unchanged
    """

    if tnode is None:
        return True, TN.TreeNode(value)
    else:
        if tnode.data is value:
            return False, tnode
        elif value < tnode.data:
            left, left_val = insert_prim(tnode.left, value)
            if left_val:
                tnode.left = left_val
                return True, tnode
            return True, tnode
        else:
            right, right_val = insert_prim(tnode.right, value)
            if right:
                tnode.right = right_val
                return True, tnode
            return True, tnode


def delete_prim(tnode, target):
    """
    Delete a value from the binary search tree.
    Preconditions:
        :param tnode: a TreeNode with the BST property
        :param target: a value
    Postconditions:
        If the value is in the tree, it is deleted.
        If the value is not there, there is no change to the tree.
    Return
        :return: tuple (flag, tree)
        flag is True if deletion succeeded;
                tree is the resulting without the value
        flag is False if the value was not in the tree,
                tree returned unchanged
    """
    def delete(tnode):
        if tnode is None:
            return False, tnode
        else:
            cval = tnode.data
            if cval == target:
                return reconnect(tnode)
            elif target < cval:
                flag, subtree = delete(tnode.left)
                if flag:
                    tnode.left = subtree
                return flag, tnode
            else:
                flag, subtree = delete(tnode.right)
                if flag:
                    tnode.right = subtree
                return flag, tnode

    def reconnect(delthis):
        if delthis.left is None and delthis.right is None:
            # the deleted node has no children
            return True, None
        elif delthis.left is None:
            # the deleted node has one child
            return True, delthis.right
        elif delthis.right is None:
            # the deleted node has one child
            return True, delthis.left
        else:
            # the deleted node has two children
            left = delthis.left
            right = delthis.right
            # walk all the way to the right from left
            walker = left
            while walker.right is not None:
                walker = walker.right
            walker.right = right
            return True, left

    return delete(tnode)

