from pickupRequest import *
from heap import *
from heapEntry import *
from graph import *
import numpy as np

class PickupScheduler:

    def __init__(self, graph, passengerTable, driverTable):
        self.graph = graph
        self.passengerTable = passengerTable
        self.driverTable = driverTable
        self.heap = DSAHeap(50)

    # -----------------------------------------------
    # Get all available drivers
    # -----------------------------------------------
    def getAvailableDrivers(self):

        availableDrivers = np.array([], dtype=object) #remove this list because cant use inbuilt list

        for entry in self.driverTable.hashArray:

            if entry.getState() == 1:
                driver = entry.getValue()
                if driver.getAvailabilityStatus() == "Available":
                    availableDrivers = np.append(availableDrivers, driver)

        return availableDrivers

    # -----------------------------------------------
    # Find nearest driver using Dijkstra
    # -----------------------------------------------
    def findNearestDriver(self, pickupLocation):

        drivers = self.getAvailableDrivers()

        if len(drivers) == 0:
            return None, None

        nearestDriver = None
        shortestTime = float('inf')

        for driver in drivers:

            start = driver.getCurrentLocation()
            result = self.graph.dijkstra(start, pickupLocation)

            if result is not None:

                T, path = result

                if T < shortestTime:
                    shortestTime = T
                    nearestDriver = driver

        return nearestDriver, shortestTime

    # -----------------------------------------------
    # Priority Formula
    # -----------------------------------------------
    def calculatePriority(self, M, T):

        if T == 0:
            T = 1

        return (6 - M) + (1000 / T)

    # -----------------------------------------------
    # Insert Pickup Request
    # -----------------------------------------------
    def addRequest(self, passengerID):

        try:
            passenger = self.passengerTable.get(str(passengerID))

        except Exception:
            print(f"Passenger {passengerID} not found")
            return

        pickupLocation = passenger.getPickupLocation()
        M = passenger.getMembershipTier()

        nearestDriver, T = self.findNearestDriver(pickupLocation)

        if nearestDriver is None:
            print("No available drivers")
            return

        priority = self.calculatePriority(M, T)

        print()
        print("=" * 60)
        print(f"Passenger: {passenger.getPassengerName()}")
        print(f"Assigned Driver: {nearestDriver.getName()}")
        print(f"Pickup Location: {pickupLocation}")
        print(f"Estimated Pickup Time (T): {T}")
        print(f"Membership Tier (M): {M}")
        print(f"Priority = (6 - {M}) + 1000/{T}")
        print(f"Priority Score = {round(priority,2)}")

        request = PickupRequest(
            passengerID,
            passenger.getPassengerName(),
            nearestDriver.getDriverID(),
            nearestDriver.getName(),
            pickupLocation,
            M,
            T,
            priority
        )

        self.heap.add(priority, request)

        print("\nHeap After Insert:")
        self.heap.printHeap()

    # -----------------------------------------------
    # Extract Highest Priority Request
    # -----------------------------------------------
    def dispatch(self):

        if self.heap.count == 0:
            print("No pickup requests available")
            return

        entry = self.heap.remove()

        request = entry.getValue()

        print()
        print("=" * 60)
        print("DISPATCHED REQUEST")
        print("=" * 60)

        print(request)

        print("\nHeap After Extraction:")
        self.heap.printHeap()

    def peek(self):
        if self.heap.count == 0:
            return None
        return self.heap.heapArr[0].getValue()