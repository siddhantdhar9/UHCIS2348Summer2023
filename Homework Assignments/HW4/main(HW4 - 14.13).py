# Siddhant Dhar - PSID: 1512852
# Zylabs 14.13: Sorting user IDs

# Global variable
num_calls = 0


# Quicksort algorithm:
# Step 1 - Pick the middle element as the pivot
# Step 2 - Compare the values using two index variables l and h (low and high)
# Step 3 - Initialized to the left and right sides of the current elements being sorted
# Step 4 - Determine if a swap is necessary


def partition(user_ids, i, k):
    # Step 1 - Pick the middle element as the pivot
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]

    # Step 2 - Compare the values using two index variables l and h (low and high)
    done = False
    l = i
    h = k
    while not done:
        # Increment low(l) while user_ids[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        # Decrement h(high) while pivot < user_ids[h]
        while pivot < user_ids[h]:
            h = h - 1

        # If there are zero or one items remaining, all numbers are partitioned. Return h
        if l >= h:
            done = True
        else:
            # Swap numbers[l] and numbers[h], update l and h
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
        return h


# Write the quicksort algorithm that recursively sorts the low and high partitions.
def quicksort(user_ids, i, k):
    # Increment the global variable num_calls in quicksort() to keep track of how many times quicksort() is called.
    global num_calls
    # Add 1 to num_calls each time quisksort() is called
    num_calls += 1
    # Base case: If there are one or zero entries to sort, partition is already sorted
    if i >= k:
        return user_ids, num_calls
    # Partition the data within the array.
    # Value j returned from partitioning is location of last item in low partition.

    j = partition(user_ids, i, k)
    # Recursively sort low partition (i to j)
    # High partition (j + 1 to k)
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return user_ids, num_calls


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
