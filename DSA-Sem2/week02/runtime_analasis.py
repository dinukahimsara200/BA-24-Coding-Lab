import time
import random
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort_timed(arr):
    """Insertion sort without print statements for clean timing"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

def generate_test_data(size, case_type):
    """Generate different types of test arrays"""
    if case_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif case_type == "sorted":
        return list(range(1, size + 1))
    elif case_type == "reverse":
        return list(range(size, 0, -1))
    elif case_type == "nearly_sorted":
        arr = list(range(1, size + 1))
        # Swap a few random elements
        for _ in range(max(1, size // 10)):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

def time_algorithm(arr):
    """Time the insertion sort algorithm"""
    arr_copy = arr.copy()  # Don't modify original
    start_time = time.perf_counter()  # More precise than time.clock()
    insertion_sort_timed(arr_copy)
    end_time = time.perf_counter()
    return end_time - start_time

def experimental_analysis():
    """Run complete experimental analysis"""
    # Test different array sizes
    sizes = [10, 50, 100, 200, 500, 1000, 2000]
    case_types = ["random", "sorted", "reverse", "nearly_sorted"]
    
    results = {case_type: {"sizes": [], "times": []} for case_type in case_types}
    
    print("Running experiments...")
    print("Size\tRandom\t\tSorted\t\tReverse\t\tNearly Sorted")
    print("-" * 70)
    
    for size in sizes:
        row_results = [str(size)]
        
        for case_type in case_types:
            # Run multiple trials and take average
            times = []
            for trial in range(5):  # 5 trials for more reliable results
                test_array = generate_test_data(size, case_type)
                elapsed_time = time_algorithm(test_array)
                times.append(elapsed_time)
            
            avg_time = sum(times) / len(times)
            results[case_type]["sizes"].append(size)
            results[case_type]["times"].append(avg_time)
            row_results.append(f"{avg_time:.6f}s")
        
        print("\t".join(row_results))
    
    return results

def plot_results(results):
    """Create plots showing time complexity"""
    plt.figure(figsize=(12, 8))
    
    # Plot 1: All cases together
    plt.subplot(2, 2, 1)
    for case_type, data in results.items():
        plt.plot(data["sizes"], data["times"], marker='o', label=case_type)
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Insertion Sort: All Cases")
    plt.legend()
    plt.grid(True)
    
    # Plot 2: Best case (sorted) vs theory
    plt.subplot(2, 2, 2)
    sizes = results["sorted"]["sizes"]
    times = results["sorted"]["times"]
    plt.plot(sizes, times, 'bo-', label="Actual (sorted)")
    # Theoretical O(n) line
    theoretical_linear = [times[0] * (n / sizes[0]) for n in sizes]
    plt.plot(sizes, theoretical_linear, 'r--', label="Theoretical O(n)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Best Case: O(n) Behavior")
    plt.legend()
    plt.grid(True)
    
    # Plot 3: Worst case (reverse) vs theory
    plt.subplot(2, 2, 3)
    sizes = results["reverse"]["sizes"]
    times = results["reverse"]["times"]
    plt.plot(sizes, times, 'ro-', label="Actual (reverse)")
    # Theoretical O(n²) line
    theoretical_quadratic = [times[0] * (n / sizes[0])**2 for n in sizes]
    plt.plot(sizes, theoretical_quadratic, 'b--', label="Theoretical O(n²)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Worst Case: O(n²) Behavior")
    plt.legend()
    plt.grid(True)
    
    # Plot 4: Log-log scale to see growth rates
    plt.subplot(2, 2, 4)
    for case_type, data in results.items():
        plt.loglog(data["sizes"], data["times"], marker='o', label=case_type)
    plt.xlabel("Input Size (n) - Log Scale")
    plt.ylabel("Time (seconds) - Log Scale")
    plt.title("Growth Rates (Log-Log Scale)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Run the complete analysis
if __name__ == "__main__":
    results = experimental_analysis()
    plot_results(results)
    
    print("\nAnalysis Complete!")
    print("\nWhat you should observe:")
    print("1. Sorted arrays (best case) show linear O(n) growth")
    print("2. Reverse sorted arrays (worst case) show quadratic O(n²) growth")
    print("3. Random arrays fall between best and worst case")
    print("4. Nearly sorted arrays perform close to best case")