class LinkedList:
    
    def __init__(self):
        self.ll = list()
        self.len = 0

    
    def get(self, index: int) -> int:
        if(index >= self.len):
            return -1
        return self.ll[index]
        

    def insertHead(self, val: int) -> None:
        head = val
        for i in range(len(self.ll)):
            tail = self.ll[i]
            self.ll[i] = head
            head = tail
        self.ll.append(head)
        self.len += 1
        

    def insertTail(self, val: int) -> None:
        self.ll.append(val)
        self.len += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.len:
            return False
        self.ll.pop(index)
        self.len -= 1
        return True
        

    def getValues(self) -> List[int]:
        return self.ll
        
