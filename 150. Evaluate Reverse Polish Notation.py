class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        # if ele is number then add to stack
        # if ele is operator then do operation on last two elements of stack
        # store result in st
        # lastly return st[0]

        for n in tokens:
            # if n is operator
            if n in ["+", "-", "*", "/"]:
                if n == "+":
                    num1 = st.pop()
                    num2 = st.pop()
                    st.append(num2 + num1)
                elif n == "-":
                    num1 = st.pop()
                    num2 = st.pop()
                    st.append(num2 - num1)
                elif n == "*":
                    num1 = st.pop()
                    num2 = st.pop()
                    st.append(num2 * num1)
                elif n == "/":
                    num1 = st.pop()
                    num2 = st.pop()
                    st.append(int(num2 / num1))

            # n is number
            else:
                st.append(int(n))
        
        return st[0]