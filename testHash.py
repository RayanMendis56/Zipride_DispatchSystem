from hashTable import *
from passenger import *
from driver import *

import time


def testHashTable():
    print("\n" + "=" * 70)
    print("MODULE 2: HASH TABLE TESTING")
    print("=" * 70)

    table = DSAHashTable(25)  # small size → forces collisions

    #-----------------------------
    # Hash table creation display
    # ----------------------------
    print("\n--- INITIAL HASH TABLE ---")
    print("Initial size :", table.size())

    # -----------------------------
    # INSERT PASSENGERS (20)
    # -----------------------------
    print("\n--- INSERTING PASSENGERS ---")

    passengers = [
        Passenger(101, "Alice", "CBD", 1),
        Passenger(102, "Bob", "Airport", 3),
        Passenger(103, "Charlie", "University", 2),
        Passenger(104, "David", "SuburbNorth", 5),
        Passenger(105, "Eva", "SuburbSouth", 4),
        Passenger(106, "Frank", "Hospital", 1),
        Passenger(107, "Grace", "ShoppingMall", 2),
        Passenger(108, "Hannah", "IndustrialPark", 3),
        Passenger(109, "Ian", "CBD", 5),
        Passenger(110, "Jack", "Airport", 4),
        Passenger(111, "Karen", "University", 1),
        Passenger(112, "Leo", "Hospital", 2),
        Passenger(113, "Mia", "ShoppingMall", 3),
        Passenger(114, "Nina", "SuburbNorth", 4),
        Passenger(115, "Owen", "SuburbSouth", 5),
        Passenger(116, "Paul", "CBD", 2),
        Passenger(117, "Quinn", "Airport", 3),
        Passenger(118, "Rose", "University", 1),
        Passenger(119, "Sam", "Hospital", 4),
        Passenger(120, "Tina", "ShoppingMall", 2),
    ]

    for p in passengers:
        table.put(p.passengerID, p)

        # Print load factor every 10 inserts
        if table.count % 10 == 0:
            print(f"Load Factor after {table.count} inserts: {table.getLoadFactor():.2f}")

    # -----------------------------
    # INSERT DRIVERS (20)
    # -----------------------------
    print("\n--- INSERTING DRIVERS ---")

    drivers = [
        Driver(201, "John", "CBD", "Available"),
        Driver(202, "Mike", "Airport", "Busy"),
        Driver(203, "Sara", "University", "Available"),
        Driver(204, "Tom", "Hospital", "Offline"),
        Driver(205, "Lily", "SuburbNorth", "Available"),
        Driver(206, "James", "SuburbSouth", "Busy"),
        Driver(207, "Emma", "ShoppingMall", "Available"),
        Driver(208, "Noah", "IndustrialPark", "Offline"),
        Driver(209, "Ava", "CBD", "Available"),
        Driver(210, "Ethan", "Airport", "Busy"),
        Driver(211, "Sophia", "University", "Available"),
        Driver(212, "Lucas", "Hospital", "Busy"),
        Driver(213, "Mason", "ShoppingMall", "Available"),
        Driver(214, "Isabella", "SuburbNorth", "Offline"),
        Driver(215, "Logan", "SuburbSouth", "Available"),
        Driver(216, "Mia", "CBD", "Busy"),
        Driver(217, "Elijah", "Airport", "Available"),
        Driver(218, "Amelia", "University", "Offline"),
        Driver(219, "Harper", "Hospital", "Available"),
        Driver(220, "Henry", "ShoppingMall", "Busy"),
    ]

    for d in drivers:
        table.put(d.driverID, d)

        if table.count % 10 == 0:
            print(f"Load Factor after {table.count} inserts: {table.getLoadFactor():.2f}")

    # check again-make separate tables and 40+ records----------------------

    # -----------------------------
    # SEARCH TESTS
    # -----------------------------
    print("\n--- SEARCH TESTS ---")

    try:
        print("Search HIT (101):", table.get(101))
    except Exception as e:
        print(e)

    try:
        print("Search HIT (205):", table.get(205))
    except Exception as e:
        print(e)

    try:
        print("Search MISS (999):", table.get(999))
    except Exception as e:
        print("Search MISS handled:", e)

    # -----------------------------
    # DELETE TESTS
    # -----------------------------
    print("\n--- DELETE TESTS ---")

    try:
        table.remove(105)
        print("Deleted key 105")
    except Exception as e:
        print(e)

    try:
        table.get(105)
    except Exception as e:
        print("Post-delete search:", e)

    try:
        table.remove(999)
    except Exception as e:
        print("Delete MISS handled:", e)

    # -----------------------------
    # COLLISION DEMONSTRATION
    # -----------------------------
    print("\n--- COLLISION DEMO ---")

    # These keys are chosen to likely collide
    keys = [1, 24, 47]  # same mod pattern if table size ~23

    for k in keys:
        try:
            table.put(k, f"CollisionTest-{k}")
        except Exception as e:
            print(e)

    # -----------------------------
    # PERFORMANCE TEST
    # -----------------------------
    print("\n--- PERFORMANCE TEST ---")

    start = time.time()

    for i in range(1000, 1100):
        table.put(i, f"Test{i}")

    end = time.time()

    print(f"Time for 100 inserts: {end - start:.6f} seconds")

    start = time.time()

    for i in range(1000, 1100):
        table.get(i)

    end = time.time()

    print(f"Time for 100 searches: {end - start:.6f} seconds")

    # -----------------------------
    # FINAL TABLE STATE
    # -----------------------------
    print("\n--- FINAL HASH TABLE ---")
    table.printTable()

    print("\n✓ Module 2 Testing Complete")


if __name__ == "__main__":
    testHashTable()