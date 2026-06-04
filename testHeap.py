from heap import DSAHeap
from pickupRequest import PickupRequest   # your class definition from pickupRequest.py
from pickupScheduler import *
from hashTable import *
from passenger import *
from driver import *

# ---------------------------------------------------
# MAIN TEST DRIVER
# ---------------------------------------------------
def main():

    print("=" * 60)
    print("MODULE 3 - HEAP BASED PICKUP SCHEDULING")
    print("=" * 60)

    # ------------------------------------------------
    # GRAPH SETUP
    # ------------------------------------------------
    graph = DSAGraph()

    locations = [
        "CBD", "Airport", "University", "SuburbNorth",
        "SuburbSouth", "ShoppingMall", "Hospital", "IndustrialPark", "IsolatedNode"
    ]

    for location in locations:
        graph.addVertex(location)

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

    # ------------------------------------------------
    # HASH TABLES
    # ------------------------------------------------
    passengerTable = DSAHashTable(31)
    driverTable = DSAHashTable(31)

    # ------------------------------------------------
    # PASSENGERS
    # ------------------------------------------------
    passengers = [
        (101, "Alice", "CBD", 1),
        (102, "Bob", "Airport", 2),
        (103, "Charlie", "University", 3),
        (104, "David", "Hospital", 4),
        (105, "Emma", "ShoppingMall", 5),
        (106, "Frank", "CBD", 2),
        (107, "Grace", "Airport", 1),
        (108, "Henry", "University", 3),
        (109, "Isabella", "Hospital", 4),
        (110, "Jack", "ShoppingMall", 5)
    ]

    for p in passengers:
        
        passenger_obj = Passenger(p[0], p[1], p[2], p[3])
        passengerTable.put(
            str(passenger_obj.getPassengerID()),
            passenger_obj
        )

    # ------------------------------------------------
    # DRIVERS
    # ------------------------------------------------
    drivers = [
        (201, "DriverA", "CBD", "Available"),
        (202, "DriverB", "Airport", "Available"),
        (203, "DriverC", "University", "Available"),
        (204, "DriverD", "Hospital", "Available"),
        (205, "DriverE", "ShoppingMall", "Busy"),
    ]

    

    for d in drivers:
        
        driver_obj = Driver(d[0], d[1], d[2], d[3])
        driverTable.put(
            str(driver_obj.getDriverID()),
            driver_obj
        )

    # ------------------------------------------------
    # CREATE SCHEDULER
    # ------------------------------------------------
    scheduler = PickupScheduler(
        graph,
        passengerTable,
        driverTable
    )

    # ------------------------------------------------
    # INSERT 10 REQUESTS
    # ------------------------------------------------
    print()
    print("=" * 60)
    print("INSERT OPERATIONS")
    print("=" * 60)

    for p in passengers:
        scheduler.addRequest(p[0])

    # ------------------------------------------------
    # EXTRACT 5 REQUESTS
    # ------------------------------------------------
    print()
    print("=" * 60)
    print("DISPATCH OPERATIONS")
    print("=" * 60)

    for i in range(5):
        scheduler.dispatch()

    print()
    print("✓ Module 3 Integrated Test Completed")


if __name__ == "__main__":
    main()
