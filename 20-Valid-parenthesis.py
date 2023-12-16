class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c in '([{':
                st.append(c)

            elif c is ')':
                if (not st or st[-1] != '('): return False
                st.pop()
            
            elif c is']':
                if (not st or st[-1] != '['): return False
                st.pop()
            
            elif c is'}':
                if (not st or st[-1] != '{'): return False
                st.pop()
        
        if not st: return True
        return False
                   