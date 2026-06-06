# COMP1002 Final Assignment – ZipRide Dispatch System

#Student Name: Rayan Mendis
#Student ID: 22731942 
#Unit:COMP1002 – Data Structures and Algorithms  

---

# Overview

The ZipRide Dispatch System is a backend ride-hailing simulation developed using fundamental data structures and algorithms. The system is divided into four integrated modules:

1. Graph-Based Route Planning
2. Hash-Based Passenger and Driver Lookup
3. Heap-Based Pickup Scheduling
4. Sorting and Analytics

These modules work together to efficiently manage passenger requests, driver assignments, route calculations, dispatch priorities, and reporting operations.

---

# Project Structure

```text
Final_Assignment/
│
├── menu.py
├── graph.py
├── linkedList.py
├── queue.py
├── stack.py
├── hashTable.py
├── passenger.py
├── driver.py
├── heap.py
├── pickupRecord.py
├── sorting.py
│
├── locations.csv
├── roads.csv
├── passengers.csv
├── drivers.csv
├── pickupRequests.csv
│
├── module1Test.py
├── module2Test.py
├── module3Test.py
├── module4Test.py
│
└── README.md
```

---

# Requirements

- Python 3.10+
- NumPy

Install NumPy:

```bash
pip install numpy
```

---

# Running the Program

Run the main system:

```bash
python menu.py
```

or

```bash
python3 menu.py
```

---

# Initial Setup

When the program starts, the user can choose between:

### Manual Setup

Allows users to enter:

- Locations
- Roads
- Passengers
- Drivers
- Pickup Requests

through keyboard input.

### CSV Setup

Loads data automatically from:

- locations.csv
- roads.csv
- passengers.csv
- drivers.csv
- pickupRequests.csv

---

# Module 1 – Graph Route Planning

## Features

- Add Location (Vertex)
- Add Road (Edge)
- Delete Location
- Delete Road
- Display Graph
- Breadth First Search (BFS)
- DFS Cycle Detection
- Dijkstra Shortest Path

## Purpose

Represents the city road network as a weighted undirected graph and calculates the shortest route between locations.

---

# Module 2 – Hash Table Lookup

## Features

### Passenger Operations

- Add Passenger
- Search Passenger
- Delete Passenger
- Display Passenger Hash Table

### Driver Operations

- Add Driver
- Search Driver
- Delete Driver
- Display Driver Hash Table

## Collision Handling

The hash table uses:

- Open Addressing
- Linear Probing

for collision resolution.

---

# Module 3 – Heap Dispatch Scheduling

## Features

- Insert Pickup Request
- Process Highest Priority Request
- Display Heap

## Priority Formula

Priority = (6 − M) + (1000 / T)

Where:

- M = Membership Tier
- T = Estimated Pickup Time

Higher priority values are dispatched first.

## Driver Assignment Strategy

1. Retrieve all available drivers from the Driver Hash Table.
2. Calculate shortest travel time using Dijkstra's Algorithm.
3. Select the nearest available driver.
4. Calculate pickup priority.
5. Insert request into the Max Heap.

---

# Module 4 – Sorting and Analytics

## Implemented Algorithms

### Merge Sort

- Stable sorting algorithm
- Time Complexity: O(n log n)

### Quick Sort

- Standard Quick Sort
- Median-of-Three Quick Sort
- Random Pivot Quick Sort

## Sorting Criteria

Pickup requests are sorted based on priority values to analyse dispatch performance.

---

# CSV File Formats

## locations.csv

```csv
Location
CBD
Airport
University
SuburbNorth
SuburbSouth
ShoppingMall
Hospital
IndustrialPark
IsolatedNode
```

## roads.csv

```csv
From,To,Weight
CBD,Airport,25
CBD,University,15
CBD,ShoppingMall,10
University,SuburbNorth,20
University,SuburbSouth,18
SuburbNorth,Hospital,12
SuburbSouth,Hospital,14
Hospital,IndustrialPark,16
Airport,IndustrialPark,30
ShoppingMall,SuburbNorth,22
SuburbNorth,SuburbSouth,8
CBD,Hospital,35
```

## passengers.csv

```csv
PassengerID,Name,PickupLocation,MembershipTier
101,Alice,CBD,1
102,Bob,Airport,2
103,Charlie,University,3
104,David,Hospital,4
105,Emma,ShoppingMall,5
106,Frank,CBD,2
107,Grace,Airport,1
108,Henry,University,3
109,Isabella,Hospital,4
110,Jack,ShoppingMall,5
```

## drivers.csv

```csv
DriverID,Name,CurrentLocation,AvailabilityStatus
201,DriverA,CBD,Available
202,DriverB,Airport,Available
203,DriverC,University,Available
204,DriverD,Hospital,Available
205,DriverE,ShoppingMall,Busy
```

## pickupRequests.csv

```csv
PassengerID,PickupLocation
101,CBD
102,Airport
103,University
104,Hospital
105,ShoppingMall
106,CBD
107,Airport
108,University
109,Hospital
110,ShoppingMall
```

---

# Test Files

## Module 1

```bash
python module1Test.py
```

Tests:

- Graph construction
- BFS traversal
- DFS cycle detection
- Dijkstra shortest path

## Module 2

```bash
python module2Test.py
```

Tests:

- Insert operations
- Search operations
- Delete operations
- Collision handling

## Module 3

```bash
python module3Test.py
```

Tests:

- Heap insertion
- Heap extraction
- Priority calculations
- Driver assignment

## Module 4

```bash
python module4Test.py
```

Tests:

- Merge Sort
- Quick Sort
- Median-of-Three Quick Sort
- Random Pivot Quick Sort

---

# Error Handling

The system handles:

- Invalid IDs
- Duplicate records
- Invalid membership tiers
- Missing graph locations
- Empty heap operations
- Invalid shortest path requests
- Hash table lookup failures

---

# Assumptions

- Graph is undirected.
- Driving times are positive values.
- Passenger IDs are unique.
- Driver IDs are unique.
- Membership tiers range from 1–5.
- Only available drivers can be assigned to requests.
- Higher priority values indicate higher dispatch urgency.

---

# References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

Curtin University. COMP1002 Data Structures and Algorithms Unit Materials.

---

# Declaration

This project was developed for the COMP1002 Final Assignment. All core data structures and algorithms including Graph, Hash Table, Heap, Merge Sort, and Quick Sort were implemented manually without using Python built-in implementations for the core logic, in accordance with assignment requirements.
