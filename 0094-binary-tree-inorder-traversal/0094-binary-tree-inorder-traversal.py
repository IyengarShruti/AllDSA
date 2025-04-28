# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach: 1.recursive-> left root append-> right. TC: O(N)
    # 2. iterative: keep going keft and if not null-> add to stack and 
    # once you get null-> pop up-> append->check for right and keep going
    # stop when: curr pointer is null and stack is empty 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 2: iterative
        stack = []
        cur = root
        res = []
        # go till stack is empty or cur is pointing to null
        while cur or stack:
            while cur:
                stack.append(cur.val)
                cur = cur.left
            # cur must be pointing to null after the loop
            cur = stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res
        """
        # 1. Approach: recursive
        res = []
        # nested function for recursive
        def inorder(root):
            # if root not present
            if not root:
                return root
            # if root is there ..then left Root right
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
            