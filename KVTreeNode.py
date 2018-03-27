# CMPT 145: Binary trees
# Defines the kv tree node ADT
#
# A KVTreeNode is a simple container with four pieces of
# information:
#   key:   the key for the node
#   value: the contained information
#   left:  a reference to another KVTreeNode, or None
#   right: a reference to another KVTreeNode, or None


# Implementation notes:
#   This ADT implementation uses a Python class


class KVTreeNode(object):
    def __init__(self, key, value, left=None, right=None):
        """
        Create a new KVTreeNode for the given data.
        Pre-conditions:
            key:    A key used to identify the node
            value:  Any data value to be stored in the KVTreeNode
            left:   Another KVTreeNode (or None, by default)
            right:  Another KVTreeNode (or None, by default)
        """
        self.value = value
        self.left = left
        self.right = right
        self.key = key

