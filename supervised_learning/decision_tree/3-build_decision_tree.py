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
        """Returns a list of all leaves under this node."""
        return (self.left_child.get_leaves_below() +
                self.right_child.get_leaves_below())


class Leaf:
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.is_leaf = True

    def get_leaves_below(self):
        """Returns a list containing only this leaf."""
        return [self]

    def __str__(self):
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    def __init__(self, root=None):
        self.root = root

    def get_leaves(self):
        """Returns a list of all leaves in the tree."""
        return self.root.get_leaves_below()
