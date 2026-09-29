class Node:
    def __init__(self, val, minVal, next=None):
        self.val = val
        self.minVal = minVal
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val,val)
        else:
            minVal = min(self.head.minVal, val)
            self.head = Node(val, minVal, self.head)

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minVal
        
