class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findLCA(root,p,q)
    def findLCA(self,node,p,q):
        if not node or node==p or node==q:
            return node
        left = self.findLCA(node.left,p,q)
        right = self.findLCA(node.right,p,q)
        
        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
