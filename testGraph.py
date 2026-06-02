from graph import *
from graphNode import *

def main():
    print()
    print("=" * 60)
    print("MODULE 1: GRAPH-BASED ROUTE PLANNING")
    print("ZipRide Dispatch System")
    print("=" * 60)

    graph = DSAGraph()

    nodes = [
        "CBD", "Airport", "University", "SuburbNorth",
        "SuburbSouth", "ShoppingMall", "Hospital", "IndustrialPark", "IsolatedNode"
    ]

    for node in nodes:
        graph.addVertex(node)

    edges = [
        ("CBD", "Airport", 25),
        ("CBD", "University", 15),
        ("CBD", "ShoppingMall", 10),
        ("University", "SuburbNorth", 20),
        ("University", "SuburbSouth", 18),
        ("SuburbNorth", "Hospital", 12),
        ("SuburbSouth", "Hospital", 14),
        ("Hospital", "IndustrialPark", 16),
        ("Airport", "IndustrialPark", 30),
        ("ShoppingMall", "SuburbNorth", 22),
        ("SuburbNorth", "SuburbSouth", 8),
        ("CBD", "Hospital", 35),
    ]

    for u, v, w in edges:
        graph.addEdge(u, v, w)

    graph.displayAsList()
    graph.displayBFS("CBD")
    graph.displayDFSCycle()

    graph.displayDijkstra("CBD", "SuburbSouth")
    graph.displayDijkstra("Airport","Hospital")

    print()
    print("✓ Module 1 graph tests complete")


if __name__ == "__main__":
    main()
