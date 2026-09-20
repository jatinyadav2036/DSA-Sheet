class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []

        def dfs(node, path):
            if not node:
                return

            # Add current node to the path
            path += str(node.val)

            # If it's a leaf, save the complete path
            if not node.left and not node.right:
                result.append(path)
                return

            # Continue to children
            path += "->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return result
