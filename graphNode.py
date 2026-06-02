from linkedList import *

class DSAGraphAdjacency:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def getVertex(self):
        return self.vertex

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight


class DSAGraphVertex:
    def __init__(self, label):
        self.label = label
        self.adjacentList = DSALinkedList()   # stores adjacent vertices and weights
        self.visited = False

    def getLabel(self):
        return self.label

    def getAdjacent(self):
        return self.adjacentList

    def addAdjacent(self, vertex, weight):
        adjacency = DSAGraphAdjacency(vertex, weight)
        self.adjacentList.insertLast(adjacency)

    def removeAdjacent(self, vertex):

        current = self.adjacentList.head

        while current:
            adjacency = current.value
            if adjacency.getVertex() == vertex:
                self.adjacentList.removeInMiddle(adjacency)
                return
            current = current.next


    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited

    def printVertex(self):
        print(f"{self.label}: ", end="")
        current = self.adjacentList.head

        while current:
            adjacency = current.value
            print(f"[{adjacency.getVertex().getLabel()}, {adjacency.getWeight()}min] ", end="")
            current = current.next

        print()