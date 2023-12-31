class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left

            node = st.pop()
            k -= 1

            if k == 0: return node.val
            curr = node.right

        