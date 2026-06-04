from heapEntry import *
import numpy as np

class DSAHeap:
    def __init__(self, size):
        self.size = size
        self.heapArr = np.array([DSAHeapEntry(None, None) for _ in range(self.size)], dtype=object)
        self.count = 0

    def add(self, priority, value):  # adds DSAheapEntry to correct place in the heap
    # start at end of arr, then trickle it up until parent is = or > priority 
        if self.count == self.size:
            raise Exception("Heap Array is Full")
        entry = DSAHeapEntry(priority,value)
        self.heapArr[self.count] = entry
        self.trickleUp(self.count)
        self.count +=1


    def remove(self):
        if self.count == 0:
            raise Exception("Heap array is empty.")
        removeEntry = self.heapArr[0]   # removing the root
        self.heapArr[0] = self.heapArr[self.count-1]  # move last element to root
        self.count -=1
        self.trickleDown(0)   
        return removeEntry

    # references -lecture slides
    def trickleUp(self,curIdx):
        parentIdx = (curIdx-1)//2
        while curIdx > 0 and self.heapArr[curIdx].getPriority() > self.heapArr[parentIdx].getPriority():
            self.heapArr[parentIdx], self.heapArr[curIdx] = self.heapArr[curIdx], self.heapArr[parentIdx]
            curIdx = parentIdx
            parentIdx = (curIdx-1)//2

    # references - lecture slides
    def trickleDown(self, curIdx):
        lChildIdx = curIdx * 2 +1
        rChildIdx = lChildIdx +1
        keepGoing = True

        while keepGoing and lChildIdx < self.count:  # is a left child
            keepGoing =  False
            largeIdx = lChildIdx   # assume left child is larger than parent
            if rChildIdx < self.count and self.heapArr[lChildIdx].getPriority() < self.heapArr[rChildIdx].getPriority():
                largeIdx = rChildIdx

            if self.heapArr[largeIdx].getPriority() > self.heapArr[curIdx].getPriority(): # if child is larger than parent, swap
                    self.heapArr[curIdx], self.heapArr[largeIdx] = self.heapArr[largeIdx], self.heapArr[curIdx]
                    keepGoing = True
                    curIdx = largeIdx
                    lChildIdx = curIdx * 2 +1
                    rChildIdx = lChildIdx + 1
            else:
                keepGoing = False  # if no swap

    def heapify(self, arr, numItems):
        self.heapArr = arr
        self.count = numItems
        for i in range((self.count//2)-1, -1, -1):
            self.trickleDown(i)


    def heapSort(self, arr):  
        self.heapArr = np.array([DSAHeapEntry(entry.getPriority(), entry.getValue()) for entry in arr])
        self.count = len(arr)
        self.heapify(self.heapArr, self.count)

        for i in range(self.count-1, 0, -1):
            self.heapArr[0], self.heapArr[i] = self.heapArr[i], self.heapArr[0]  # max value is sent to the end
            self.count -=1
            self.trickleDown(0)

        self.count = len(arr)
        # in this function, priority is actually stored in ascending order, not depending
        return self.heapArr   # return sorted arr
    

    def printHeap(self):
        print()
        print("Current Heap Contents:")
        for i in range(self.count):
            priority = self.heapArr[i].getPriority()
            value = self.heapArr[i].getValue()
            print(f" {i}. priority= {priority}, value= {value}")

        print()
    
    def peek(self):
        if self.count == 0:
            raise Exception("Heap array is empty.")
        return self.heapArr[0]