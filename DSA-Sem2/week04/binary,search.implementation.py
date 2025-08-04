def binary_search(arr, target, left, right):
    if left > right:
        return False  # Target not found
    mid = (left + right) // 2
    if arr[mid] == target:
        return True  # Target found
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)  # Search left half
    else:
        return binary_search(arr, target, mid + 1, right)  # Search right half

# Example Usage
if __name__ == "__main__":
    # Test cases
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target1 = 7
    target2 = 8
    
    # Search for 7 (exists)
    print(f"Is {target1} in the array? {binary_search(sorted_array, target1, 0, len(sorted_array)-1)}")  # Output: True
    
    # Search for 8 (does not exist)
    print(f"Is {target2} in the array? {binary_search(sorted_array, target2, 0, len(sorted_array)-1)}")  # Output: False
    
    # Edge case: Empty array
    empty_array = []
    print(f"Is 5 in an empty array? {binary_search(empty_array, 5, 0, len(empty_array)-1)}")  # Output: False
    
    # Edge case: Single-element array (match)
    single_array = [4]
    print(f"Is 4 in [4]? {binary_search(single_array, 4, 0, len(single_array)-1)}")  # Output: True