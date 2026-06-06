#
# DSA Menu for ZipRide Dispatch System
# Student Name: Nigamuni Sandul Rayan Mendis
# 

from graph import *
from hashTable import *
from heap import *
from passenger import *
from driver import *
from heap import *
from sorting import *
from pickupRecord import *


def setupSystem():

    graph = DSAGraph()

    passengerTable = DSAHashTable(30)

    driverTable = DSAHashTable(30)

    heap = DSAHeap(50)

    print()
    print("+---------------------------------------------------------------+")
    print("|\t\t\tZIPRIDE DISPATCH SYSTEM\t\t\t|")
    print("+---------------------------------------------------------------+")
    print("|\t\t\t\t\t\t\t\t|")
    print("|\t\t1. Load Data From CSV Files\t\t\t|")
    print("|\t\t2. Manual Data Entry\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t|")
    print("+---------------------------------------------------------------+")

    choice = int(input("Enter option: "))

    
    if choice == 1:

        loadGraphFromCSV(graph)

        loadPassengersFromCSV(passengerTable)

        loadDriversFromCSV(driverTable)

        loadPickupRequestsFromCSV(
            graph,
            passengerTable,
            driverTable,
            heap
        )

        print()
        print("Data loaded successfully from CSV files...")


    elif choice == 2:

        manualSetup(graph,passengerTable,driverTable,heap)

        print()
        print("Manual setup completed...")

    else:

        print("Invalid option")

    return graph, passengerTable, driverTable, heap


# User input functions for manual setup of graph, hash tables and heap with pickup requests
def manualSetup(graph, passengerTable, driverTable, heap):

    # ---------------- LOCATIONS ----------------

    numLocations = int(input("How many locations? "))

    for i in range(numLocations):

        location = input(f"Enter location {i+1}: ")

        graph.addVertex(location)
        print("Location added successfully")
        print()

    # ---------------- ROADS ----------------

    numRoads = int(input("How many roads? "))

    for i in range(numRoads):

        fromLoc = input("From: ")
        toLoc = input("To: ")
        weight = int(input("Weight: "))

        graph.addEdge(fromLoc, toLoc, weight)
        print("Road added successfully")
        print()

    # ---------------- PASSENGERS ----------------

    numPassengers = int(input("How many passengers? "))

    for i in range(numPassengers):

        passengerID = input("Passenger ID: ")
        name = input("Name: ")
        pickupLocation = input("Pickup Location: ")
        tier = int(input("Membership Tier (1-5): "))

        passenger = Passenger(
            int(passengerID),
            name,
            pickupLocation,
            tier
        )

        passengerTable.put(passengerID, passenger)
        print("Passenger added successfully")
        print()

    # ---------------- DRIVERS ----------------

    numDrivers = int(input("How many drivers? "))

    for i in range(numDrivers):

        driverID = input("Driver ID: ")
        name = input("Name: ")
        location = input("Location: ")
        status = input("Status (Available/Busy/Offline): ")

        driver = Driver(
            int(driverID),
            name,
            location,
            status
        )

        driverTable.put(driverID, driver)
        print("Driver added successfully")
        print()

    # ---------------- PICKUP REQUESTS ----------------

    numRequests = int(input("How many pickup requests? "))

    for i in range(numRequests):

        print()
        print(f"Pickup Request {i+1}")

        passengerID = input("Passenger ID: ")
        pickupLocation = input("Pickup Location: ")

        try:

            passenger = passengerTable.get(passengerID)

            membershipTier = passenger.getMembershipTier()

            nearestDriver = None
            nearestDistance = float("inf")

            # FIND NEAREST AVAILABLE DRIVER
            for entry in driverTable.hashArray:

                if entry.getState() == 1:

                    driver = entry.getValue()

                    if driver.getAvailabilityStatus() == "Available":

                        distance, path = graph.dijkstra(
                            driver.getCurrentLocation(),
                            pickupLocation
                        )

                        if distance is not None and distance < nearestDistance:

                            nearestDistance = distance
                            nearestDriver = driver

            # INSERT INTO HEAP
            if nearestDriver is not None:

                priority = calculatePriority(
                    membershipTier,
                    nearestDistance
                )

                request = PickupRecord(
                    passenger,
                    nearestDriver,
                    pickupLocation,
                    priority,
                    nearestDistance
                )

                heap.add(priority, request)

                print("Pickup request added to heap")
                print()

            else:

                print("No available driver found")
                print()

        except Exception as e:

            print(e)
    



def loadPickupRequestsFromCSV(graph,passengerTable,driverTable,heap):

    file = open("pickupRequests.csv", "r")

    next(file)

    for line in file:

        passengerID, pickupLocation = line.strip().split(",")

        passenger = passengerTable.get(passengerID)

        membershipTier = passenger.getMembershipTier()

        nearestDriver = None
        nearestDistance = float("inf")

        for entry in driverTable.hashArray:

            if entry.getState() == 1:

                driver = entry.getValue()

                if driver.getAvailabilityStatus() == "Available":

                    distance, path = graph.dijkstra(
                        driver.getCurrentLocation(),
                        pickupLocation
                    )

                    if distance is not None and distance < nearestDistance:

                        nearestDistance = distance
                        nearestDriver = driver

        if nearestDriver is not None:

            priority = calculatePriority(
                membershipTier,
                nearestDistance
            )

            request = PickupRecord(
                passenger,
                nearestDriver,
                pickupLocation,
                priority,
                nearestDistance
            )

            heap.add(priority, request)

    file.close()

def loadDriversFromCSV(driverTable):

    file = open("drivers.csv", "r")

    next(file)

    for line in file:

        driverID, name, location, status = line.strip().split(",")

        driver = Driver(
            int(driverID),
            name,
            location,
            status
        )

        driverTable.put(driverID, driver)

    file.close()

def loadPassengersFromCSV(passengerTable):

    file = open("passengers.csv", "r")

    next(file)

    for line in file:

        passengerID, name, pickupLocation, tier = line.strip().split(",")

        passenger = Passenger(
            int(passengerID),
            name,
            pickupLocation,
            int(tier)
        )

        passengerTable.put(passengerID, passenger)

    file.close()


def loadGraphFromCSV(graph):

    # LOAD LOCATIONS
    file = open("locations.csv", "r")

    next(file)

    for line in file:

        location = line.strip()

        if location != "":
            graph.addVertex(location)

    file.close()

    # LOAD ROADS
    file = open("roads.csv", "r")

    next(file)

    for line in file:

        fromLoc, toLoc, weight = line.strip().split(",")

        graph.addEdge(fromLoc, toLoc, int(weight))

    file.close()


# ----------------------------------------------------------
# MODULE 3 HELPER
# ----------------------------------------------------------
def calculatePriority(M, T):
        if T == 0:
            T = 1

        return (6 - M) + (1000 / T)


# ----------------------------------------------------------
# MAIN MENU      
# ----------------------------------------------------------
def main():

    graph, passengerTable, driverTable, heap = setupSystem()

    choice = 0

    while choice != 5:

        print()
        print("+---------------------------------------------------------------+")
        print("|\t\t\tZIPRIDE DISPATCH SYSTEM\t\t\t|")
        print("+---------------------------------------------------------------+")
        print("|\t\t\t\t\t\t\t\t|")
        print("|\t\t1. Module 1 - Graph Route Planning\t\t|")
        print("|\t\t2. Module 2 - Hash Tables Lookup\t\t|")
        print("|\t\t3. Module 3 - Heap Dispatch Scheduling\t\t|")
        print("|\t\t4. Module 4 - Sorting & Analytics\t\t|")
        print("|\t\t5. Exit\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t\t|")
        print("+---------------------------------------------------------------+")
        print()
        

        choice = int(input("Select Module: "))
        print()

        # ----------------------------------------------------------
        # MODULE 1
        # ----------------------------------------------------------
        if choice == 1:

            moduleChoice = 0

            while moduleChoice != 9:

                print()
                print("+---------------------------------------------------------------+")
                print("|\t\tModule1-Graph Route Planning\t\t\t|")
                print("+---------------------------------------------------------------+")
                print("|\t\t\t\t\t\t\t\t|")
                print("|\t\t\t1. Display Graph\t\t\t|")
                print("|\t\t\t2. Add Location\t\t\t\t|")
                print("|\t\t\t3. Add Road\t\t\t\t|")
                print("|\t\t\t4. Delete Location\t\t\t|")
                print("|\t\t\t5. Delete Road\t\t\t\t|")
                print("|\t\t\t6. BFS Traversal\t\t\t|")
                print("|\t\t\t7. DFS Cycle Detection\t\t\t|")
                print("|\t\t\t8. Dijkstra Shortest Path\t\t|")
                print("|\t\t\t9. Back\t\t\t\t\t|")
                print("|\t\t\t\t\t\t\t\t|")
                print("+---------------------------------------------------------------+")
                print()
                

                moduleChoice = int(input("Enter choice: "))
                print()

                # DISPLAY GRAPH
                if moduleChoice == 1:
                    graph.displayAsList()

                # ADD LOCATION
                elif moduleChoice == 2:

                    try:

                        location = input("Enter new location: ")

                        graph.addVertex(location)

                        print("Location added successfully")

                    except Exception as e:

                        print(e)
                
                # ADD ROAD
                elif moduleChoice == 3:

                    try:

                        fromLoc = input("From location: ")
                        toLoc = input("To location: ")
                        weight = int(input("Road weight/distance: "))

                        graph.addEdge(fromLoc, toLoc, weight)

                        print("Road added successfully")

                    except Exception as e:

                        print(e)

                # DELETE LOCATION
                elif moduleChoice == 4:

                    try:

                        location = input("Enter location to delete: ")

                        graph.removeVertex(location)

                        print("Location deleted successfully")

                    except Exception as e:

                        print(e)

                # DELETE ROAD
                elif moduleChoice == 5:

                    try:

                        fromLoc = input("From location: ")
                        toLoc = input("To location: ")

                        graph.removeEdge(fromLoc, toLoc)

                        print("Road deleted successfully")

                    except Exception as e:

                        print(e)
                        
                # BFS
                elif moduleChoice == 6:

                    start = input("Enter start location: ")

                    try:
                        graph.displayBFS(start)
                    except Exception as e:
                        print(e)

                # DFS
                elif moduleChoice == 7:
                    graph.displayDFSCycle()

                # DIJKSTRA
                elif moduleChoice == 8:
                    start = input("Enter start location: ")
                    end = input("Enter destination: ")

                    try:
                        distance, path = graph.dijkstra(start, end)

                        if distance is None:
                            print("No path found")
                        else:

                            print()
                            print(f"Shortest Distance: {distance} minutes")

                            print("Path: ", end="")

                            current = path.head

                            while current:
                                print(current.value.getLabel(), end="")
                                if current.next:
                                    print(" -> ", end="")
                                current = current.next
                            print()

                    except Exception as e:
                        print(e)

                elif moduleChoice == 9:
                    print("Returning to Main Menu...")

                else:
                    print("Invalid choice")

        # ----------------------------------------------------------
        # MODULE 2
        # ----------------------------------------------------------
        elif choice == 2:

            moduleChoice = 0

            while moduleChoice != 9:

                print()
                print("+---------------------------------------------------------------+")
                print("|\t\tModule2-Hash Table Lookup\t\t\t|")
                print("+---------------------------------------------------------------+")
                print("|\t\t\t\t\t\t\t\t|")
                print("|\t\t1. Add Passeneger\t\t\t\t|")
                print("|\t\t2. Add Driver\t\t\t\t\t|")
                print("|\t\t3. Search Passenger\t\t\t\t|")
                print("|\t\t4. Search Driver\t\t\t\t|")
                print("|\t\t5. Delete Passenger\t\t\t\t|")
                print("|\t\t6. Delete Driver\t\t\t\t|")
                print("|\t\t7. Display Passenger Hashtable\t\t\t|")
                print("|\t\t8. Display Driver HashTable\t\t\t|")
                print("|\t\t9. Back\t\t\t\t\t\t|")
                print("|\t\t\t\t\t\t\t\t|")
                print("+---------------------------------------------------------------+")
                print()
                

                moduleChoice = int(input("Enter choice: "))
                print()

                # ADD PASSENGER
                if moduleChoice == 1:

                    try:

                        passengerID = input("Passenger ID: ")
                        name = input("Passenger Name: ")
                        pickupLocation = input("Pickup Location: ")
                        membershipTier = int(input("Membership Tier (1-5): "))

                        passenger = Passenger(
                            int(passengerID),
                            name,
                            pickupLocation,
                            membershipTier
                        )

                        passengerTable.put(passengerID, passenger)

                        print()
                        print("Passenger added successfully")

                    except Exception as e:
                        print(e)

                # ADD DRIVER
                elif moduleChoice == 2:

                    try:

                        driverID = input("Driver ID: ")
                        name = input("Driver Name: ")
                        location = input("Current Location: ")
                        status = input("Availability Status: ")

                        driver = Driver(
                            int(driverID),
                            name,
                            location,
                            status
                        )

                        driverTable.put(driverID, driver)

                        print()
                        print("Driver added successfully")

                    except Exception as e:
                        print(e)

                # SEARCH PASSENGER
                if moduleChoice == 3:

                    passengerID = input("Enter Passenger ID: ")

                    try:
                        passenger = passengerTable.get(passengerID)
                        print()
                        print(passenger)

                    except Exception as e:
                        print(e)

                # SEARCH DRIVER
                elif moduleChoice == 4:

                    driverID = input("Enter Driver ID: ")

                    try:
                        driver = driverTable.get(driverID)
                        print()
                        print(driver)

                    except Exception as e:
                        print(e)

                # DELETE PASSENGER
                elif moduleChoice == 5:

                    passengerID = input("Enter Passenger ID to delete: ")

                    try:
                        passengerTable.remove(passengerID)
                        print("Passenger deleted successfully")

                    except Exception as e:
                        print(e)

                # DELETE DRIVER
                elif moduleChoice == 6:

                    driverID = input("Enter Driver ID to delete: ")

                    try:
                        driverTable.remove(driverID)
                        print("Driver deleted successfully")

                    except Exception as e:
                        print(e)

                
                # DISPLAY PASSENGER HASH TABLE
                elif moduleChoice == 7:

                    print()
                    print("=" * 60)
                    print("PASSENGER HASH TABLE")
                    print("=" * 60)

                    passengerTable.printTable()

                
                # DISPLAY DRIVER HASH TABLE
                elif moduleChoice == 8:

                    print()
                    print("=" * 60)
                    print("DRIVER HASH TABLE")
                    print("=" * 60)

                    driverTable.printTable()

                # EXIT
                elif moduleChoice == 9:
                    print("Returning to Main Menu...")

                else:
                    print("Invalid choice")

        # ----------------------------------------------------------
        # MODULE 3
        # ----------------------------------------------------------
        elif choice == 3:

            moduleChoice = 0

            while moduleChoice != 4:

                print()
                print("+---------------------------------------------------------------+")
                print("|\t\tModule3-Heap Dispatch System\t\t\t|")
                print("+---------------------------------------------------------------+")
                print("|\t\t\t\t\t\t\t\t|")
                print("|\t\t1. Insert Pickup Request\t\t\t|")
                print("|\t\t2. Process Highest Priority Request\t\t|")
                print("|\t\t3. Display Heap\t\t\t\t\t|")
                print("|\t\t4. Back\t\t\t\t\t\t|")
                print("|\t\t\t\t\t\t\t\t|")
                print("+---------------------------------------------------------------+")
                print()

                moduleChoice = int(input("Enter choice: "))
                print()

                # INSERT PICKUP
                if moduleChoice == 1:

                    passengerID = input("Passenger ID: ")
                    pickupLocation = input("Pickup Location: ")

                    try:

                        passenger = passengerTable.get(passengerID)

                        membershipTier = passenger.getMembershipTier()

                        nearestDriver = None
                        nearestDistance = float("inf")

                        current = driverTable.hashArray

                        for entry in current:

                            if entry.getState() == 1:

                                driver = entry.getValue()

                                if driver.getAvailabilityStatus() == "Available":

                                    distance, path = graph.dijkstra(
                                        driver.getCurrentLocation(),
                                        pickupLocation
                                    )

                                    if distance is not None and distance < nearestDistance:
                                        nearestDistance = distance
                                        nearestDriver = driver

                        if nearestDriver is None:
                            print("No available drivers")
                        else:

                            priority = calculatePriority(
                                membershipTier,
                                nearestDistance
                            )

                            request = PickupRecord(
                                passenger,
                                nearestDriver,
                                pickupLocation,
                                priority,
                                nearestDistance
                            )

                            heap.add(priority, request)

                            print()
                            print("Pickup Request Added")
                            print(f"Assigned Driver: {nearestDriver.getName()}")
                            print(f"Distance: {nearestDistance}")
                            print(f"Priority: {priority}")

                    except Exception as e:
                        print(e)

                # PROCESS REQUEST
                elif moduleChoice == 2:

                    try:

                        removed = heap.peek()

                        request = removed.getValue()

                        print()
                        print("=" * 50)
                        print("PROCESSING PICKUP REQUEST")
                        print("=" * 50)

                        print(request)

                    except Exception as e:
                        print(e)

                # DISPLAY HEAP
                elif moduleChoice == 3:
                    heap.printHeap()

                elif moduleChoice == 4:
                    print("Returning to Main Menu...")

                else:
                    print("Invalid choice")

        # ----------------------------------------------------------
        # MODULE 4
        # ----------------------------------------------------------
        elif choice == 4:

            moduleChoice = 0

            while moduleChoice != 5:

                print()
                print("+---------------------------------------------------------------+")
                print("|\t\tModule4-Sorting & Analytics\t\t\t|")
                print("+---------------------------------------------------------------+")
                print("|\t\t\t\t\t\t\t\t|")
                print("|\t\t1. Merge Sort\t\t\t\t\t|")
                print("|\t\t2. Quick Sort\t\t\t\t\t|")
                print("|\t\t3. Median-of-Three Quick Sort\t\t\t|")
                print("|\t\t4. Random Pivot Quick Sort\t\t\t|")
                print("|\t\t5. Back\t\t\t\t\t\t|")
                print("|\t\t\t\t\t\t\t\t|")
                print("+---------------------------------------------------------------+")  
                print()

                moduleChoice = int(input("Enter choice: "))
                print()

                # ---------------------------------------------
                # BUILD ARRAY FROM HEAP PRIORITIES
                # ---------------------------------------------
                arr=[]

                for i in range(heap.count):
                    arr.append(heap.heapArr[i].getPriority())

                # Check whether heap has data
                if len(arr) == 0:

                    print()
                    print("No pickup requests in heap to sort.")
                    

                # ---------------------------------------------
                # MERGE SORT
                # ---------------------------------------------
                if moduleChoice == 1:

                    print()
                    print("=" * 50)
                    print("MERGE SORT")
                    print("=" * 50)

                    print("Original Priorities:")
                    for request in arr:
                        print(request.__str__())

                    mergeSort(arr)

                    print()
                    print("Sorted Priorities:")
                    for request in arr:
                        print(request.__str__())

                # ---------------------------------------------
                # QUICK SORT
                # ---------------------------------------------
                elif moduleChoice == 2:

                    print()
                    print("=" * 50)
                    print("QUICK SORT")
                    print("=" * 50)

                    print("Original Priorities:")
                    for request in arr:
                        print(request.__str__())

                    quickSort(arr)

                    print()
                    print("Sorted Priorities:")
                    for request in arr:
                        print(request.__str__())

                # ---------------------------------------------
                # MEDIAN OF THREE QUICK SORT
                # ---------------------------------------------
                elif moduleChoice == 3:

                    print()
                    print("=" * 50)
                    print("MEDIAN-OF-THREE QUICK SORT")
                    print("=" * 50)

                    print("Original Priorities:")
                    for request in arr:
                        print(request.__str__())

                    quickSortMedian3(arr)

                    print()
                    print("Sorted Priorities:")
                    for request in arr:
                        print(request.__str__())

                # ---------------------------------------------
                # RANDOM PIVOT QUICK SORT
                # ---------------------------------------------
                elif moduleChoice == 4:

                    print()
                    print("=" * 50)
                    print("RANDOM PIVOT QUICK SORT")
                    print("=" * 50)

                    print("Original Priorities:")
                    for request in arr:
                        print(request.__str__())

                    quickSortRandom(arr)

                    print()
                    print("Sorted Priorities:")
                    for request in arr:
                        print(request.__str__())

                # ---------------------------------------------
                # BACK
                # ---------------------------------------------
                elif moduleChoice == 5:

                    print("Returning to Main Menu...")

                else:

                    print("Invalid choice")

        # ----------------------------------------------------------
        # EXIT
        # ----------------------------------------------------------
        elif choice == 5:

            print()
            print("Exiting ZipRide Dispatch System...")
            print("Goodbye!")

        else:
            print("Invalid choice")


# ----------------------------------------------------------
# RUN PROGRAM
# ----------------------------------------------------------
if __name__ == "__main__":
    main()