# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        def level_traverse(root,lev,val_lev):
            if not root: return
            if lev not in val_lev.keys():
                val_lev[lev]=[root.val]
            else: val_lev[lev]+=[root.val]
            level_traverse(root.left,lev+1,val_lev)
            level_traverse(root.right,lev+1,val_lev)
            return val_lev
        ans=[]
        for i in level_traverse(root,0,{}).values():ans.append(i) 
        return ans[::-1]