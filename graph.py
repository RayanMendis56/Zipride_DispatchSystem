# from tracemalloc import start

from graphNode import *
from stacksAndQueues import *
from linkedList import *

import numpy as np

class DSAGraph:
    """Weighted undirected graph using linked lists."""

    def __init__(self):
        self.labels = DSALinkedList() # stores all vertices in the graph
        self.vertexCount = 0
        self.edgeCount = 0

    def getVertexCount(self):
        return self.vertexCount

    def getEdgeCount(self):
        return self.edgeCount

    def addVertex(self, label):
        if self.hasVertex(label):
            raise ValueError(f"Vertex {label} already exists")

        new_vertex = DSAGraphVertex(label)
        self.labels.insertToMiddle(new_vertex)
        self.vertexCount += 1
        return new_vertex

    def getVertex(self, label):
        current = self.labels.head
        while current is not None:
            if current.value.getLabel() == label:
                return current.value
            current = current.next
        return None

    def hasVertex(self, label):
        return self.getVertex(label) is not None

    def addEdge(self, label1, label2, weight):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)

        if weight <= 0:
            raise ValueError("Edge weight must be a positive integer")

        if vertex1 is None:
            raise ValueError(f"Vertex {label1} does not exist")
        if vertex2 is None:
            raise ValueError(f"Vertex {label2} does not exist")
        if vertex1 == vertex2:
            raise ValueError("Cannot create self-loop")

        current = vertex1.getAdjacent().head
        while current is not None:
            adjacency = current.value
            if adjacency.getVertex() == vertex2:
                return
            current = current.next

        vertex1.addAdjacent(vertex2, weight)
        vertex2.addAdjacent(vertex1, weight)
        self.edgeCount += 1

    def removeEdge(self, label1, label2):

        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)

        if vertex1 is None and vertex2 is None:
            raise ValueError(f"Vertices {label1} and {label2} do not exist")
        
        elif vertex1 is None:
            raise ValueError(f"Vertex {label1} does not exist")

        elif vertex2 is None:
            raise ValueError(f"Vertex {label2} does not exist")

        vertex1.removeAdjacent(vertex2)
        vertex2.removeAdjacent(vertex1)

        self.edgeCount -= 1

    def removeVertex(self, label):

        vertex = self.getVertex(label)

        if vertex is None:
            raise ValueError("Vertex does not exist")

        # REMOVE ALL CONNECTED EDGES
        current = self.labels.head

        while current:

            otherVertex = current.value
            if otherVertex != vertex:
                otherVertex.removeAdjacent(vertex)
            current = current.next

        # REMOVE VERTEX FROM LABEL LIST
        self.labels.removeInMiddle(vertex)

        self.vertexCount -= 1


    def displayAsList(self):
        print()
        current = self.labels.head
        while current is not None:
            current.value.printVertex()
            current = current.next
        print()

    def clearVisited(self):
        current = self.labels.head
        while current is not None:
            current.value.clearVisited()
            current = current.next

    def breadthFirstSearch(self, start_label):
        if self.getVertexCount() == 0:
            raise ValueError("Cannot do BFS on an empty graph")

        start_vertex = self.getVertex(start_label)
        if start_vertex is None:
            raise ValueError(f"Start vertex {start_label} does not exist")

        self.clearVisited()

        Q = DSAQueue()
        levels = DSALinkedList()

        # level 0
        start_vertex.setVisited()
        Q.enqueue((start_vertex, 0))

        while not Q.isEmpty():
            vertex, level = Q.dequeue()

            # find or create level node
            current = levels.head
            level_node = None
            while current and level_node is None:
                if current.value[0] == level:
                    level_node = current.value
                current = current.next

            if level_node is None:
                level_node = (level, DSALinkedList())
                levels.insertLast(level_node)

            # add vertex to level list
            level_node[1].insertLast(vertex)

            # traverse neighbors
            cur = vertex.getAdjacent().head
            while cur:
                neighbour = cur.value.getVertex()
                if not neighbour.getVisited():
                    neighbour.setVisited()
                    Q.enqueue((neighbour, level + 1))
                cur = cur.next

        return levels
    

    def displayBFS(self, start_label):
        print("\n" + "=" * 60)
        print(f"BFS from node: {start_label}")
        print("=" * 60)

        levels = self.breadthFirstSearch(start_label)
        current = levels.head

        while current:
            level, vertex_list = current.value
            print(f"Level {level}: ", end="")

            cur = vertex_list.head
            while cur:
                print(cur.value.getLabel(), end=" ")
                cur = cur.next
            print()

            current = current.next

        print("=" * 60)


    def depthFirstSearch(self, start_label):
        if self.getVertexCount() == 0:
            raise ValueError("Cannot do DFS on an empty graph")

        start_vertex = self.getVertex(start_label)
        if start_vertex is None:
            raise ValueError(f"Start vertex {start_label} does not exist")

        self.clearVisited()

        S = DSAStack()
        S.push(start_vertex)
        start_vertex.setVisited()

        print("\nDFS Traversal:")

        while not S.isEmpty():
            vertex = S.pop()
            print(vertex.getLabel(), end=" ")

            cur = vertex.getAdjacent().head
            while cur:
                neighbour = cur.value.getVertex()
                if not neighbour.getVisited():
                    neighbour.setVisited()
                    S.push(neighbour)
                cur = cur.next

        print()


    def _dfsCycleHelper(self, vertex, parent, cycle_list):
        vertex.setVisited()
        current_adj = vertex.getAdjacent().head

        while current_adj is not None:
            adjacency = current_adj.value
            neighbour = adjacency.getVertex()
            if not neighbour.getVisited():
                if self._dfsCycleHelper(neighbour, vertex, cycle_list):
                    cycle_list.insertFirst(vertex)
                    return True
            elif neighbour != parent:
                cycle_list.insertFirst(vertex)
                cycle_list.insertFirst(neighbour)
                return True
            current_adj = current_adj.next

        return False

    def hasCycle(self):
        self.clearVisited()
        current = self.labels.head

        while current is not None:
            vertex = current.value
            if not vertex.getVisited():
                cycle_list = DSALinkedList()
                if self._dfsCycleHelper(vertex, None, cycle_list):
                    return True, cycle_list
            current = current.next

        return False, None

    def displayDFSCycle(self):
        print()
        print("=" * 60)
        print("DFS - CYCLE DETECTION")
        print("=" * 60)
        found, cycle_list = self.hasCycle()
        if found:
            labels = np.array([], dtype=object)
            current = cycle_list.head
            while current is not None:
                labels = np.append(labels, current.value.getLabel())
                current = current.next
            print("✓ Cycle FOUND in graph")
            print(f"Cycle members: {labels}")
        else:
            print("✓ No cycle detected in graph")
        print("=" * 60)

    def _getDistanceRecord(self, vertex):
        current = self.distances.head
        while current is not None:
            if current.value.vertex == vertex:
                return current.value
            current = current.next
        return None

    def _getPathRecord(self, vertex):
        current = self.paths.head
        while current is not None:
            if current.value.vertex == vertex:
                return current.value
            current = current.next
        return None
    

    def dijkstra(self, startLabel, endLabel):

        if self.getVertexCount() == 0:
            raise ValueError("Graph is empty")

        start = self.getVertex(startLabel)
        end = self.getVertex(endLabel)

        if start is None or end is None:
            raise ValueError("Start or end vertex does not exist")

        # Special case
        if start == end:
            path = DSALinkedList()
            path.insertLast(start)
            return 0, path

        # -------------------------------
        # Step 1: Initialize using numpy arrays
        # -------------------------------

        vertices = np.array([], dtype=object)
        distances = np.array([], dtype=float)
        previous = np.array([], dtype=object)
        visited = np.array([], dtype=bool)

        current = self.labels.head

        while current:
            vertex = current.value

            vertices = np.append(vertices, vertex)
            distances = np.append(distances, float('inf'))
            previous = np.append(previous, None)
            visited = np.append(visited, False)

            current = current.next

        # Set start distance = 0
        startIndex = np.where(vertices == start)[0][0]
        distances[startIndex] = 0

        # -------------------------------
        # Step 2: Main Dijkstra Loop
        # -------------------------------

        for _ in range(self.getVertexCount()):

            minDistance = float('inf')
            minIndex = -1

            # Find smallest unvisited vertex
            for i in range(len(vertices)):
                if not visited[i] and distances[i] < minDistance:
                    minDistance = distances[i]
                    minIndex = i

            # No reachable vertices left - only continue if valid vertex found
            if minIndex != -1:
                visited[minIndex] = True
                currentVertex = vertices[minIndex]

            # Relax all adjacent edges
            adj = currentVertex.getAdjacent().head

            while adj:

                adjacency = adj.value
                neighbour = adjacency.getVertex()
                weight = adjacency.getWeight()

                neighbourIndex = np.where(vertices == neighbour)[0][0]

                if not visited[neighbourIndex]:

                    newDistance = distances[minIndex] + weight

                    if newDistance < distances[neighbourIndex]:
                        distances[neighbourIndex] = newDistance
                        previous[neighbourIndex] = currentVertex

                adj = adj.next

        # -------------------------------
        # Step 3: Build Path
        # -------------------------------

        endIndex = np.where(vertices == end)[0][0]

        if distances[endIndex] == float('inf'):
            return None, None

        path = DSALinkedList()
        currentVertex = end

        while currentVertex is not None:

            path.insertFirst(currentVertex)

            currentIndex = np.where(vertices == currentVertex)[0][0]
            currentVertex = previous[currentIndex]

        return distances[endIndex], path
    

    
    def displayDijkstra(self, startLabel, endLabel):
        print("\n" + "=" * 60)
        print(f"Dijkstra: {startLabel} → {endLabel}")
        print("=" * 60)

        distance, path = self.dijkstra(startLabel, endLabel)

        if distance is None:
            print("No path found")
            return

        print(f"Shortest Time: {distance} minutes")
        print("Path: ", end="")

        cur = path.head
        while cur:
            print(cur.value.getLabel(), end=" ")
            cur = cur.next

        print("\n" + "=" * 60)


 