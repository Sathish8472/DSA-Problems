# Approach 3: Constant Space with Encoded Values (Advanced)
# time: O(1), Space: O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        elif val >= self.min_val:
            self.stack.append(val)
        else:
            self.stack.append(2 * val - self.min_val)
            self.min_val = val

    def pop(self) -> None:
        top = self.stack.pop()
        if top < self.min_val:
            self.min_val = 2 * self.min_val - top

    def top(self) -> int:
        top = self.stack[-1]
        return top if top >= self.min_val else self.min_val

    def getMin(self) -> int:
        return self.min_val 

# Approach 1: tuple: (val, min_so_far)
# Space: O(N)
class MinStack2:
    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        if not self.stack:
            min_val = val 
        else:
            min_val = min(val, self.stack[-1][1])
        self.stack.append((val, min_val))
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> None:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]

# Approach 2: Two Stacks (Main + Min Stack)
class MinStack1:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped_val = self.stack.pop()
            if self.min_stack and popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()