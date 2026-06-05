from pickupRecord import *

import numpy as np
import random


# =========================================================
# MERGE SORT
# =========================================================

def mergeSort(A):

    mergeSortRec(A, 0, len(A) - 1)


def mergeSortRec(A, leftIdx, rightIdx):

    if leftIdx < rightIdx:

        midIdx = (leftIdx + rightIdx) // 2

        mergeSortRec(A, leftIdx, midIdx)
        mergeSortRec(A, midIdx + 1, rightIdx)

        merge(A, leftIdx, midIdx, rightIdx)


def merge(A, leftIdx, midIdx, rightIdx):

    tempArr = np.empty(
        (rightIdx - leftIdx + 1),
        dtype=object
    )

    ii = leftIdx
    jj = midIdx + 1
    kk = 0

    while ii <= midIdx and jj <= rightIdx:

        if (A[ii]<= A[jj]):
            tempArr[kk] = A[ii]
            ii += 1
        else:
            tempArr[kk] = A[jj]
            jj += 1

        kk += 1

    while ii <= midIdx:

        tempArr[kk] = A[ii]
        ii += 1
        kk += 1

    while jj <= rightIdx:

        tempArr[kk] = A[jj]
        jj += 1
        kk += 1

    for idx in range(len(tempArr)):

        A[leftIdx + idx] = tempArr[idx]


# =========================================================
# QUICK SORT
# =========================================================

def quickSort(A):

    quickSortRec(A, 0, len(A) - 1)


def quickSortRec(A, leftIdx, rightIdx):

    if rightIdx > leftIdx:

        pivotIdx = medianOfThree(
            A,
            leftIdx,
            rightIdx
        )

        newPivotIdx = doPartitioning(
            A,
            leftIdx,
            rightIdx,
            pivotIdx
        )

        quickSortRec(A, leftIdx, newPivotIdx - 1)

        quickSortRec(A, newPivotIdx + 1, rightIdx)

# =========================================================
# QUICK SORT (Median-of-Three)
# =========================================================

def quickSortMedian3(A):
    """ quickSortMedian3 - front-end for kick-starting the recursive algorithm with median-of-three pivot selection
    """
    quickSortMedian3Recurse(A, 0, len(A) - 1)


def quickSortMedian3Recurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = medianOfThree(A, leftIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx) # Partition around the median pivot

        quickSortMedian3Recurse(A, leftIdx, newPivotIdx - 1) 
        quickSortMedian3Recurse(A, newPivotIdx + 1, rightIdx)



def medianOfThree(A, leftIdx, rightIdx):

    midIdx = (leftIdx + rightIdx) // 2

    if A[leftIdx] > A[midIdx]:
        A[leftIdx], A[midIdx] = A[midIdx], A[leftIdx]

    if A[leftIdx] > A[rightIdx]:
        A[leftIdx], A[rightIdx] = A[rightIdx], A[leftIdx]

    if A[midIdx] > A[rightIdx]:
        A[midIdx], A[rightIdx] = A[rightIdx], A[midIdx]

    return midIdx


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):

    pivotVal = A[pivotIdx]

    A[pivotIdx], A[rightIdx] = A[rightIdx], A[pivotIdx]

    currIdx = leftIdx

    for i in range(leftIdx, rightIdx):

        if A[i] < pivotVal:

            A[i], A[currIdx] = A[currIdx], A[i]
            currIdx += 1

    A[rightIdx], A[currIdx] = A[currIdx], A[rightIdx]

    return currIdx

# =========================================================
# QUICK SORT (Random-Pivot)
# =========================================================
def quickSortRandom(A):
    """
    Front-end for Random Pivot Quick Sort
    """
    quickSortRandomRecurse(A, 0, len(A) - 1)


def quickSortRandomRecurse(A, leftIdx, rightIdx):

    if leftIdx < rightIdx:

        # Select random pivot
        pivotIdx = random.randint(leftIdx, rightIdx)

        # Partition array
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        # Recursively sort left side
        quickSortRandomRecurse(A, leftIdx, newPivotIdx - 1)

        # Recursively sort right side
        quickSortRandomRecurse(A, newPivotIdx + 1, rightIdx)