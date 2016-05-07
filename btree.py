import copy
from board import Board
from bt_node import *

class BTree:
    """
    Represent a binary tree.
    """
    def __init__(self, root=None):
        """Initialize root of binary tree"""
        self._root = root

    def expand(self):
        """Expand node"""
        self._expand_node(self._root, -1)

    def _expand_node(self, node, item):
        """
        This method creates two random steps for game, saves them, makes two moves.
        """
        bnd = node.get_board()
        bnd1 = copy.deepcopy(bnd)
        bnd2 = copy.deepcopy(bnd)
        i1, j1 = bnd.make_random_move()
        i2, j2 = bnd.make_random_move()
        bnd1.set_value((i1, j1), item)
        bnd2.set_value((i2, j2), item)
        nd1 = BTNode(bnd1)
        nd2 = BTNode(bnd2)
        node.left = nd1
        node.right = nd2
        item = -item       #shows whose turn is
        if bnd1.still_have_move() and bnd1.has_winner() == None:
            self._expand_node(nd1, item)
        elif bnd2.still_have_move() and bnd2.has_winner() == None:
            self._expand_node(nd2, item)

    def get_best_move(self):
        """
        Do best move
        """
        val_1 = self._compute_value(self._root.left)
        val_2 = self._compute_value(self._root.right)
        if val_1 < val_2:
            return self._root.left.get_board()
        else:
            return self._root.right.get_board()

    def _compute_value(self, node):
        """
        Compute value of node in best case.
        """
        bnd = node.get_board()
        if bnd.has_winner == None and bnd.still_have_move:
            return self._compute_value(node.left) + self._compute_value(node.right)
        else:
            return bnd.has_winner()