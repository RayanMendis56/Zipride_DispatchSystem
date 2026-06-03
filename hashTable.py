from hashEntry import *

import numpy as np

class DSAHashTable:
    def __init__(self, size):
        self.actualsize = self.nextPrime(size)
        self.count = 0
        self.hashArray = np.array([DSAHashEntry() for _ in range(self.actualsize)], dtype=object)


    def nextPrime(self, startVal):
        
        if startVal <= 2:
            primeVal = 2
            return primeVal
        #Make sure the entered value is an odd number
        elif startVal % 2 == 0:  
            primeVal = startVal + 1
        else: 
            primeVal = startVal  

        while True:
            isPrime = True
            if primeVal %2 == 0 and primeVal !=2:
                isPrime = False
            else:
                i = 3
                rootVal = primeVal ** 0.5

                while i <= rootVal and isPrime:
                    if primeVal % i == 0:
                        isPrime = False
                    else:
                        i += 2
            if not isPrime:
                primeVal +=2
            else:
                return primeVal

    # ---------- LOAD FACTOR ----------
    def getLoadFactor(self):
        return self.count / self.actualsize

    # ---------- HASH ----------
    def hash(self, key):
        key = str(key)
        hashIdx = 0
        for char in key:
            hashIdx = (hashIdx * 31 + ord(char)) % self.actualsize
        return hashIdx

    def stepHash(self, key):
        key = str(key)
        hashIdx = 0
        for char in key:
            hashIdx = (17 * hashIdx + ord(char))
        return (hashIdx % (self.actualsize - 1)) + 1

    # ---------- INSERT ----------
    def put(self, key, value):
        print(f"Inserting: {key}")

        idx = self.hash(key)
        step = self.stepHash(key)

        probe = 0
        inserted = False

        while probe < self.actualsize and not inserted:
            entry = self.hashArray[idx]

            if entry.state != 1:  # empty or deleted
                self.hashArray[idx] = DSAHashEntry.with_values(key, value)
                self.count += 1
                inserted = True

            elif entry.key == key:
                raise KeyError("Duplicate key")

            else:
                print(f"Collision at {idx} → probing...")
                idx = (idx + step) % self.actualsize
                probe += 1

        if not inserted:
            raise Exception("Hash table full")

        # Resize if needed
        if self.getLoadFactor() > 0.7:
            self.resize(self.actualsize * 2)

    # ---------- SEARCH ----------
    def get(self, key):
        idx = self.hash(key)
        step = self.stepHash(key)

        probe = 0

        while probe < self.actualsize:
            entry = self.hashArray[idx]

            if entry.state == 0:
                break # replace this part because can't use break keyword ----------------

            elif entry.state == 1 and entry.key == key:
                return entry.value

            idx = (idx + step) % self.actualsize
            probe += 1

        raise KeyError(f"{key} not found")

    # ---------- DELETE ----------
    def remove(self, key):
        idx = self.hash(key)
        step = self.stepHash(key)

        probe = 0
        found = False

        while probe < self.actualsize and not found:
            entry = self.hashArray[idx]

            if entry.state == 0:
                found = False
                probe = self.actualsize

            elif entry.state == 1 and entry.key == key:
                entry.setState(-1)
                self.count -= 1
                print(f"Removed {key}")
                found = True

            else:
                idx = (idx + step) % self.actualsize
                probe += 1

        if not found:
            raise KeyError(f"{key} not found")

    # ---------- RESIZE ----------
    def resize(self, newSize):
        print(f"Resizing table → {newSize}")

        oldArray = self.hashArray
        self.actualsize = self.nextPrime(newSize)
        self.hashArray = np.array([DSAHashEntry() for _ in range(self.actualsize)], dtype=object)
        self.count = 0

        for entry in oldArray:
            if entry.state == 1:
                self.put(entry.key, entry.value)

    # ---------- DEBUG ----------
    def printTable(self):
        print("\nHash Table:")
        for i in range(self.actualsize):
            print(f"{i}: {self.hashArray[i]}")

    def size(self):
        return self.actualsize