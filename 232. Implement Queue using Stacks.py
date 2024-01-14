class MyQueue:

    def __init__(self):
        self.in_s = []
        self.out_s = []
        
    def push(self, x: int) -> None:
        self.in_s.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.out_s.pop()
        

    def peek(self) -> int:
        if not self.out_s:
            while self.in_s:
                self.out_s.append(self.in_s.pop())
        return self.out_s[-1]
        

    def empty(self) -> bool:
        return not self.in_s and not self.out_s