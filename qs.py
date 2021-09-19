# Merge sort algorithm
# Import requirements
from prettytable import PrettyTable
import random
import time

# Initialize table
x = PrettyTable()

# Declare function
def mergeSort(alist):
    print("Splitting ",alist)

    # Loop for splitting into two halves

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # Initialize variables

        i=0
        j=0
        k=0

        # Loops for two half comparisons

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

# Fill list with n random numbers between 1 - 99

n = 10000
alist = random.sample(range(0, 10000), n)
mergeSort(alist)

# print list
print(alist)


# Function for time analysis
def measure():
    start_time = time.time()
    mergeSort(alist)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(time_elapsed)
    print(n)
    # Correcting decimal places to 3
    print(round(time_elapsed, 3))
    time_elapsed_third = (round(time_elapsed, 3))
    # Fill row of table
    x.add_column("10000", [time_elapsed_third])
    print(x)


if __name__ == "__main__":
    measure()