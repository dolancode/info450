# Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.

import json

'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(list, low_ind, high_ind):
    if low_ind < high_ind:
        partition_index = partition(list, low_ind, high_ind)
        quicksort(list, low_ind, partition_index - 1)
        quicksort(list, partition_index + 1, high_ind)


def swap(list, ind_a, ind_b):
    (list[ind_a], list[ind_b]) = (list[ind_b], list[ind_a])


def partition(list, low_ind, high_ind):

    pivot = list[high_ind]

    partition_ind = low_ind - 1

    for ind in range(low_ind, high_ind):
        if list[ind] <= pivot:

            partition_ind += 1
            swap(list, partition_ind, ind)

    swap(list, partition_ind + 1, high_ind)

    return partition_ind + 1


def main():
    # WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM,
    # AND WRITE OUT YOUR FILE

    with open('numbers.txt') as f:
        lines = f.read()
        res = json.loads(lines)
        quicksort(res, 0, len(res)-1)

    return  # WHAT DOES IT RETURN?


if __name__ == "__main__":
    main()
