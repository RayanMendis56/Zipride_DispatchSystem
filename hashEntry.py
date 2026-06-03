class DSAHashEntry:
    def __init__(self, key="", value=None, state=0):
        self.key = key
        self.value = value
        self.state = state  # 0-empty, 1-used, -1-deleted

    @classmethod
    def with_values(cls, key, value):
        return cls(key, value, 1)
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value 
             
    def getState(self):
        return self.state
    
    def setState(self, newState):
        self.state = newState

    def __str__(self):
        return f"Key: {self.key}, Value: {self.value}, State: {self.state}"