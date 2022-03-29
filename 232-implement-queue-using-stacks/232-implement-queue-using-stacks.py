class MyQueue:

    def __init__(self):
        self._in = []    # 입력용
        self._out = []   # 출력용
        
    def push(self, x: int) -> None:
        self._in.append(x)
    
    # 출력용 stack에 옮겨서 첫번째로 입력한 값 pop
    def pop(self) -> int:
        self.peek()
        return self._out.pop()

    # 입력용 stack의 값 출력용 stack으로 옮기고 첫번째 원소 return
    def peek(self) -> int:
        # 출력용 stack에 있는 값을 모두 처리한 경우에만 입력용 stack으로 옮기기
        if not self._out: 
            while self._in:
                self._out.append(self._in.pop())
        return self._out[-1]

    def empty(self) -> bool:
        return len(self._out) == 0 and len(self._in) == 0
    
        
            
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()