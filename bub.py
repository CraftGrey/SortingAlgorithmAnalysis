# Bubble sort algorithm
# Import requirements
from prettytable import PrettyTable
import random
import time

# Initialize table
x = PrettyTable()


def bubble_sort(my_list):

    # The list is iterated through the amount of times that there is components of the list
    for i in range(len(my_list)):

        # The last pair of entries will be (n-2, n-1)
        for t in range(len(my_list) - 1):
            if my_list[t] > my_list[t+1]:

                # Then swap the elements
                my_list[t], my_list[t+1] = my_list[t+1], my_list[t]


# Fill list with n random numbers between
# Change value for n and range for testing time complexity
n = 10000
my_list = random.sample(range(0, 10000), n)
bubble_sort(my_list)
print(my_list)

# Function for time analysis
def measure():
    start_time = time.time()
    bubble_sort(my_list)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(n)
    # Correcting decimal places to 3
    print(round(time_elapsed, 8))
    time_elapsed_third = (round(time_elapsed, 3))
    # Fills row of table
    # change value in "" to n
    x.add_column("10000", [time_elapsed_third])
    print(x)


if __name__ == "__main__":
    measure()

