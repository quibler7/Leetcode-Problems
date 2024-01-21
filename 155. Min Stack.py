class MinStack:

    def __init__(self):
        self.st = []
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        self.st.append(val)
        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        mini = float('inf')
        for n in self.st:
            if n < mini:
                mini = n
        return mini
        