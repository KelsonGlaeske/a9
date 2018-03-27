# CMPT 145: Binary trees
# Defines the tree node ADT
#
# A treenode is a simple container with three attributes
#   data: the contained information
#   left:  a reference to another treenode or None
#   right: a reference to another treenode or None


class TreeNode(object):

    def __init__(self, data, left=None, right=None):
        """
        Create a new treenode for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the treenode
            left, right:  Another treenode (or None, by default)
        Post-condition:
            none
        """
        self.data = data
        self.left = left
        self.right = right

