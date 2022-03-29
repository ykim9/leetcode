class MyQueue:

    def __init__(self):
        self._in = []    # 입력용
        self._out = []   # 출력용
        
    def push(self, x: int) -> None:
        self._in.append(x)
    
    # 출력용 stack에 옮겨서 첫번째로 입력한 값 pop
    def pop(self) -> int:
        self.in_to_out()
        return self._out.pop()

    def peek(self) -> int:
        self.in_to_out()
        return self._out[-1]

    def empty(self) -> bool:
        self.in_to_out()
        return len(self._out) == 0
    
    # 입력용 stack의 값 출력용 stack으로 옮기기
    def in_to_out(self):
        # 출력용 stack에 이전에 넣은 값이 아직 있으면 처리하지 않기
        if self._out: 
            return
        
        while self._in:
            self._out.append(self._in.pop())
            
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()