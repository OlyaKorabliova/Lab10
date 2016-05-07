class BTNode:

    """Represent node for a binary tree"""

    def __init__(self, data):
        """Initialize data of node and its left & right child."""
        self.data = data
        self.right = self.left = None

    def get_board(self):
        """Return board"""
        return self.data

    def __str__(self):
        return str(self.data)