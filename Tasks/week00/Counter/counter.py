########################################################
# counter.py
# Developer: Christofer Rostedt
# Date:
########################################################
class Counter:
    counter: int

    def __init__(self):
        self.counter = 0

    def addCount(self) -> None:
        self.counter += 1
        return None
    
    def getCount(self) -> int:
        return self.counter
    
    def zeroCount(self) -> None:
        self.counter = 0
        return None