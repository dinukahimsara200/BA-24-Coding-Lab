import time
import random
import matplotlib.pyplot as plt

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
    sizes = [100, 500, 1000, 3000, 5000, 7000, 10000]
    
    # Store timing results
    best_times = []
    worst_times = []
    avg_times = []
    
    # Print table header
    print("\nInsertion Sort Runtime Analysis")
    print("=" * 60)
    print(f"{'Size':<10} {'Best Case (sorted)':<20} {'Worst Case (reverse)':<20} {'Average Case (random)':<20}")
    print("-" * 60)
    
    for n in sizes:
        # Best case
        arr_best = list(range(n))
        start = time.time()
        insertionSort(arr_best)
        best_time = time.time() - start
        best_times.append(best_time)
        
        # Worst case
        arr_worst = list(range(n, 0, -1))
        start = time.time()
        insertionSort(arr_worst)
        worst_time = time.time() - start
        worst_times.append(worst_time)
        
        # Average case
        arr_avg = random.sample(range(n), n)
        start = time.time()
        insertionSort(arr_avg)
        avg_time = time.time() - start
        avg_times.append(avg_time)
        
        # Print results for this size
        print(f"{n:<10} {best_time:<20.6f} {worst_time:<20.6f} {avg_time:<20.6f}")
    
    # Generate the plot (clean without time labels)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, best_times, 'g-', label='Best Case (Sorted)', linewidth=2)
    plt.plot(sizes, worst_times, 'r-', label='Worst Case (Reverse)', linewidth=2)
    plt.plot(sizes, avg_times, 'b--', label='Average Case (Random)', linewidth=2)
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort Runtime Analysis')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('insertion_sort_runtime.png', dpi=300)
    plt.show()

# Run the test
test_runtime()