import random
import time
import copy

from pickupRecord import *
from sorting import *


# =========================================================
# GENERATE RANDOM RECORDS
# =========================================================

def generatePickupRecords(size):

    locations = [
        "CBD",
        "Airport",
        "University",
        "Hospital",
        "ShoppingMall",
        "IndustrialPark"
    ]

    records = []

    for i in range(size):

        requestID = i + 1

        passengerName = f"Passenger{i+1}"

        pickupLocation = random.choice(locations)

        driverName = f"Driver{i+1}"

        estimatedPickupTime = random.randint(1, 60)

        record = PickupRecord(
            requestID,
            passengerName,
            pickupLocation,
            driverName,
            estimatedPickupTime
        )

        records.append(record)

    return records


# =========================================================
# CREATE NEARLY SORTED DATASET
# =========================================================

def makeNearlySorted(records):

    mergeSort(records)

    swaps = len(records) // 10

    for _ in range(swaps):

        idx1 = random.randint(0, len(records)-1)
        idx2 = random.randint(0, len(records)-1)

        records[idx1], records[idx2] = (
            records[idx2],
            records[idx1]
        )

    return records


# =========================================================
# CREATE REVERSED DATASET
# =========================================================

def makeReversed(records):

    mergeSort(records)

    left = 0
    right = len(records) - 1

    while left < right:

        records[left], records[right] = (
            records[right],
            records[left]
        )

        left += 1
        right -= 1

    return records


# =========================================================
# PRINT FIRST FEW RECORDS
# =========================================================

def printSample(records, amount=5):

    for i in range(min(amount, len(records))):

        print(records[i])


# =========================================================
# MAIN TEST DRIVER
# =========================================================

def main():

    random.seed(100)

    datasetSizes = [100, 500, 1000]

    conditions = [
        "Random",
        "Nearly Sorted",
        "Reversed"
    ]

    for size in datasetSizes:

        print()
        print("=" * 70)
        print(f"DATASET SIZE: {size}")
        print("=" * 70)

        baseData = generatePickupRecords(size)

        for condition in conditions:

            print()
            print("-" * 70)
            print(f"Condition: {condition}")
            print("-" * 70)

            # -------------------------------------------------
            # CREATE DATA CONDITION
            # -------------------------------------------------

            if condition == "Random":

                dataset = copy.deepcopy(baseData)

            elif condition == "Nearly Sorted":

                dataset = makeNearlySorted(
                    copy.deepcopy(baseData)
                )

            elif condition == "Reversed":

                dataset = makeReversed(
                    copy.deepcopy(baseData)
                )

            # -------------------------------------------------
            # MERGE SORT TEST
            # -------------------------------------------------

            mergeData = copy.deepcopy(dataset)

            startTime = time.perf_counter()

            mergeSort(mergeData)

            endTime = time.perf_counter()

            mergeTime = endTime - startTime

            # -------------------------------------------------
            # QUICK SORT TEST
            # -------------------------------------------------

            quickData = copy.deepcopy(dataset)

            startTime = time.perf_counter()

            quickSort(quickData)

            endTime = time.perf_counter()

            quickTime = endTime - startTime

            # -------------------------------------------------
            # OUTPUT RESULTS
            # -------------------------------------------------

            print()
            print("Merge Sort Time:")
            print(f"{mergeTime:.6f} seconds")

            print()
            print("Quick Sort Time:")
            print(f"{quickTime:.6f} seconds")

            print()
            print("First 5 Sorted Records:")
            printSample(quickData)

    print()
    print("=" * 70)
    print("MODULE 4 TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()