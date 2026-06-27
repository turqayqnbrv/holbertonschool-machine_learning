#!/usr/bin/env python3

class Node:
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, depth=0, is_root=False):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.depth = depth
        self.is_root = is_root
        self.is_leaf = False

    def get_leaves_below(self):
        """
        Recursively traverse the tree to collect all leaf nodes.
        Calls this method on both children and concatenates the results.
        """
        return (self.left_child.get_leaves_below() +
                self.right_child.get_leaves_below())


class Leaf:
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.is_leaf = True

    def get_leaves_below(self):
        """
        Base case for recursion: return a list containing this leaf itself.
        """
        return [self]

    def __str__(self):
        """String representation of the leaf for display purposes."""
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    def __init__(self, root=None):
        self.root = root

    def get_leaves(self):
        """
        Public interface to retrieve all leaves from the root of the tree.
        """
        # Starts the recursive process from the root node
        return self.root.get_leaves_below()
