#!/usr/bin/env python3

"""
Decision Tree Components
Includes classes for nodes (both decision and leaf nodes) and the
decision tree itself.
"""
import numpy as np


class Node:
    """
    Represents a decision node in a decision tree, which can split data based
    on features and thresholds.
    """
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """
        Initializes the node with optional feature splits, threshold values,
        children, root status, and depth.
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        Returns the maximum depth of the tree beneath this node.
        """
        max_depth = self.depth

        if self.left_child is not None:
            max_depth = max(max_depth, self.left_child.max_depth_below())

        if self.right_child is not None:
            max_depth = max(max_depth, self.right_child.max_depth_below())

        return max_depth

    def count_nodes_below(self, only_leaves=False):
        """
        Counts the nodes in the subtree rooted at this node.
        Optionally counts only leaf nodes.
        """
        if only_leaves:
            if self.is_leaf:
                return 1
            
            count = 0
            if self.left_child is not None:
                count += self.left_child.count_nodes_below(only_leaves=True)
            if self.right_child is not None:
                count += self.right_child.count_nodes_below(only_leaves=True)
            return count

        # Count all nodes (internal nodes + leaves)
        count = 1
        if self.left_child is not None:
            count += self.left_child.count_nodes_below(only_leaves=False)
        if self.right_child is not None:
            count += self.right_child.count_nodes_below(only_leaves=False)
        return count
