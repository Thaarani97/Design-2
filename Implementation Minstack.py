#TC
# push,pop,top,getMin O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
       
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)
            
        
    def pop(self) -> None:
        pop_ele = self.stack.pop()
        if pop_ele == self.minstack[-1]:
            self.minstack.pop()
            
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]