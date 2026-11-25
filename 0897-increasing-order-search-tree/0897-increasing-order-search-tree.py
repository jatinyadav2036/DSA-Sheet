
class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(0)
        curr = [dummy]

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            node.left = None
            curr[0].right = node
            curr[0] = node

            inorder(node.right)

        inorder(root)

        return dummy.right
