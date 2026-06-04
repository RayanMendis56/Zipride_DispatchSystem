class DSAHeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
