class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        def sameTree(a, b):
            # Both are empty
            if not a and not b:
                return True

            # One is empty, or values differ
            if not a or not b or a.val != b.val:
                return False

            # Check both subtrees
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        # Check every possible starting node in root
        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)
