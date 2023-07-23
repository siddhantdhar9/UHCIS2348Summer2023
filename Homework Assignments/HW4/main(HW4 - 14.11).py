# Siddhant Dhar - PSID: 1512852
# Zylabs 14.11: Descending selection sort with output during execution

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        # Find index of largest remaining element
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j
        # Use selection sort to swap numbers[i] and numbers[index_largest]
        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp
        for num in numbers:
            print(num, end=" ")
        print()
    return numbers


if __name__ == "__main__":
    numbers = [int(num) for num in input("").split()]
    selection_sort_descend_trace(numbers)