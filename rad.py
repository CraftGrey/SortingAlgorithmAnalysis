# Radix sort algorithm
# Import requirements
from prettytable import PrettyTable
import random
import time

# Initialize table
x = PrettyTable()


def countingSort(arr, abc):

    # Define n as array length
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * n

    # Define count array as 0
    count = [0] * 10

    # Store count of ints in count[]
    for j in range(0, n):
        index = (arr[j] / abc)
        count[int(index % 10)] += 1

    # Change count[i], it now contains position of this digit in output array
    for j in range(1, 10):
        count[j] += count[j - 1]

    # Output array
    j = n - 1
    while j >= 0:
        index = (arr[j] / abc)
        output[count[int(index % 10)] - 1] = arr[j]
        count[int(index % 10)] -= 1
        j -= 1

    # Copying the output array to arr[] array now has sorted numbers
    j = 0
    for j in range(0, len(arr)):
        arr[j] = output[j]


# Radix sort method
def radixSort(arr):

    # Find the maximum number
    max1 = max(arr)

    # Do counting sort for every int where i is the current number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10


# Fill list with n random numbers between
# Change value for n and range for testing time complexity
n = 10000
arr = random.sample(range(0, 10000), n)

# Call function
radixSort(arr)

for j in range(len(arr)):
    print(arr[j])


# Function for time analysis
def measure():
    start_time = time.time()
    radixSort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(n)
    # Correcting decimal places to 3
    print(round(time_elapsed, 3))
    time_elapsed_third = (round(time_elapsed, 3))
    # Fill row of table
    x.add_column("10000", [time_elapsed_third])
    print(x)


if __name__ == "__main__":
    measure()

