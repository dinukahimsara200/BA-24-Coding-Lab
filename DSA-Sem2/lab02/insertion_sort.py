def insertionSort(arr):
    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(arr)):
        # Store the current element to be compared and inserted
        key = arr[i]
        # Initialize a pointer to traverse the sorted portion of the array
        j = i

        # Shift elements of the sorted portion (arr[0..i-1]) that are greater than 'key'
        # to the right by one position to make space for 'key'
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]  # Move the larger element one position ahead
            j -= 1              # Move the pointer leftwards to check the previous element

        # Insert 'key' into its correct position in the sorted portion
        arr[j] = key

    return arr  # Return the sorted array

# Test Cases:
print(insertionSort([5, 2, 4, 6, 1, 3]))  # Output: [1, 2, 3, 4, 5, 6]
print(insertionSort([30, 10, 20, 50, 40]))  # Output: [10, 20, 30, 40, 50]