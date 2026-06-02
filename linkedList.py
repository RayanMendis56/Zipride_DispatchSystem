class DSAListNode:                            
    def __init__(self, label):
        self.value = label  # of type DSAGraphVertex
        self.next = None  # no prev pointer because it is a single ended linked list

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value


class DSALinkedList:
    def __init__(self):
        self.head = None  # Only head pointer, no tail for single-ended
       
    def isEmpty(self):
        return self.head is None

    def insertFirst(self,newVal):
        newNode = DSAListNode(newVal)
        newNode.next = self.head
        self.head = newNode

    def insertLast(self, newVal):
        newNode = DSAListNode(newVal)  # newVal is of type DSAGraphVertex
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def insertToMiddle(self, newVal):  # newVal is of type DSAGraphVertex
        newNode = DSAListNode(newVal)
        label = newVal.getLabel()

        if self.isEmpty() or label <= self.head.value.getLabel():
            self.insertFirst(newVal)
            return
        
        current = self.head
        while current.next is not None and current.next.value.getLabel() < label:
            current = current.next
            
        newNode.next = current.next   # inserting Last is happening here, if it exists the loop when current.next is None
        current.next = newNode

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Cannot peek first - list is empty")
        return self.head.value
    
    def findValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Cannot remove from empty list")
        value = self.head.value
        self.head = self.head.next
        return value
    
    def removeLast(self):
        if self.isEmpty():
            raise Exception("Cannot remove from empty list")
        
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
            
        current = self.head
        while current.next.next is not None:
            current = current.next
            
        value = current.next.value
        current.next = None
        return value
    

    def removeInMiddle(self, RemoveVal):
        if self.isEmpty():
            raise Exception("Cannot remove from empty list")
        
        # RemoveFirst is happening
        if self.head.value == RemoveVal:
            removed = self.head
            self.head = self.head.next
            return removed
        
        current = self.head
        while current.next is not None:
            if current.next.value == RemoveVal:
                removed = current.next
                current.next = current.next.next
                return removed
            current = current.next
        
        return None  # Return None instead of raising exception

    def getIndex(self, value):  # Returns index of value node
        count = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return count
            current = current.next
            count += 1
        raise Exception(f"Value {value} not found in list")
    
    def getValueOfIndex(self, index):
        if index < 0:
            raise Exception("Index cannot be negative.")
        count = 0
        current = self.head
        while current is not None:
            if count == index:
                return current.getValue()
            current = current.next
            count +=1
        raise Exception("Index out of bounds")
  

    def printLinkedList(self):
        current = self.head
        if current is None:
            print("Linked List is empty")
            return
            
        print("Linked List Printing Structure")
        printStr = ""
        while current is not None:
            printStr += f" {current.value.printDSAGraphVertex()} <->"
            current = current.next
        print(printStr[:-3])  # Remove the last arrow
        print()


    def printLinkedListQueue(self):
        cur = self.head
        if cur is None:
            raise Exception("Linkded List (Queue) is empty")
        printStr = ""
        while cur is not None:
            curVal = cur.value.getLabel()
            printStr += f"({curVal} , "
            cur = cur.next
            if cur is not None:
                curVal = cur.value.getLabel()
                printStr += f"{curVal}) "
                cur = cur.next            
        print(printStr)