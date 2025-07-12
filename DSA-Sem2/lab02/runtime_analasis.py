import time
import random   # For generating random arrays
import matplotlib.pyplot as plt     # For plotting the results

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr

def test_runtime():
    
    """
    Measures and compares the runtime of insertionSort for different cases,
    printing results to terminal and showing a clean graph.
    """
    
    # Input sizes to test
    sizes = [900, 1750, 3100, 4500]
    
    # Store timing results
    best_times = []
    worst_times = []
    avg_times = []
    
    # Print table header
    print("\nInsertion Sort Runtime Analysis")
    print("=" * 60)
    print(f"{'Size':<10} {'Best Case (sorted)':<20} {'Worst Case (reverse)':<20} {'Average Case (random)':<20}") #
    print("-" * 60)
    
    for n in sizes:
        # Best case
        arr_best = list(range(n))            # Already sorted array
        t_start = time.time()                # Start timer
        insertionSort(arr_best)              # Run insertion sort
        t_end = time.time()                  # End timer
        best_time_elapsed = t_end - t_start  # Calculate elapsed time
        best_times.append(best_time_elapsed) # Store best case time
        
        # Worst case
        arr_worst = list(range(n, 0, -1)) # Reverse sorted array
        t_start = time.time()
        insertionSort(arr_worst)
        t_end = time.time()
        worst_time_elapsed = t_end - t_start
        worst_times.append(worst_time_elapsed)
        
        # Average case
        arr_avg = random.sample(range(n), n) # Random array
        t_start = time.time()
        insertionSort(arr_avg)
        t_end = time.time()
        avg_time_elapsed = t_end - t_start
        avg_times.append(avg_time_elapsed)
        
        # Print results for this size
        print(f"{n:<10} {best_time_elapsed:<20.6f} {worst_time_elapsed:<20.6f} {avg_time_elapsed:<20.6f}")
    
    # Generate the plot (clean without time labels)
    plt.figure(figsize=(10, 6))                                                    # Create a figure with specified size
    plt.plot(sizes, best_times, 'g-', label='Best Case (Sorted)', linewidth=2)     # Plot best-case times in green solid line
    plt.plot(sizes, worst_times, 'r-', label='Worst Case (Reverse)', linewidth=2)  # Plot worst-case times in red solid line
    plt.plot(sizes, avg_times, 'b--', label='Average Case (Random)', linewidth=2)  # Plot average-case times in blue dashed line
    
    # Set plot labels and title
    plt.xticks(sizes)  # Set x-ticks to the sizes for better readability
    plt.xlabel('Input Size (n)') 
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort Runtime Analysis')
    plt.grid(True, linestyle='--', alpha=0.7) # Add grid for better readability
    plt.legend() 
    
    plt.tight_layout()                                 # Adjust layout to prevent overlap
    plt.savefig('insertion_sort_runtime.png', dpi=300) # Save the plot as a PNG file with high resolution
    plt.show() 

test_runtime()