class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # Compare current node with previous node in sorted order
            if self.prev is not None:
                self.min_diff = min(
                    self.min_diff,
                    node.val - self.prev
                )

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff
