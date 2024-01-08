import queue
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0

        q = queue.Queue()
        q.put(root)
        res = 0

        while not q.empty():
            curr = q.get()
            if curr.val >= low and curr.val <= high: 
                res += curr.val 

            if curr.left: q.put(curr.left)
            if curr.right: q.put(curr.right)
        
        return res

