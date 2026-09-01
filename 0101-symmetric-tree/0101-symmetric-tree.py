class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        # If both are null, they are symmetric
        if not t1 and not t2:
            return True
        # If only one is null, they are not symmetric
        if not t1 or not t2:
            return False
        # The values must match, and their cross-subtrees must match
        return (t1.val == t2.val) and \
               self.isMirror(t1.left, t2.right) and \
               self.isMirror(t1.right, t2.left)
