class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        l = []
        def preorder(node):
            if node is None:
                return
            l.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        curr = root

        for i in range(1, len(l)):
            curr.left = None
            curr.right = TreeNode(l[i])
            curr = curr.right

    
                