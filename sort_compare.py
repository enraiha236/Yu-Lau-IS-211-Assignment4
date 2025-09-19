import random
import time

def time_function (func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end-start

#Insertion sort: Builds a sorted list by repeatedly taking the next element and inserting it in the correct position.
def insertion_sort (alist):
    for index in range (1,len(alist)):
        current_value = alist[index]
        position = index

        while position >0 and alist[position - 1] > current_value:
            alist[position] = alist[position -1]
            position = position -1

        alist[position] = current_value
    return alist

#Shell sort algorithm: Uses a gap sequence to compare and sort elements far apart, then reduces the gap.
def shell_sort(alist):
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for start in range(sublist_count):
            for i in range(start + sublist_count, len(alist), sublist_count):
                current_value = alist[i]
                position = i
                while position >= sublist_count and alist[position - sublist_count] > current_value:
                    alist[position] = alist[position - sublist_count]
                    position = position - sublist_count
                alist[position] = current_value
        sublist_count = sublist_count // 2
    return alist

def python_sort (alist):
    alist.sort()
    return alist

def benchmark(func, name, list_sizes, trials=100):
    """Run benchmark for a given function across list sizes."""
    for size in list_sizes:
        times = []
        for _ in range(trials):
            alist = [random.randint(1, size * 10) for _ in range(size)]
            _, t = time_function(func, alist[:])  # copy so sorting doesn’t affect next trial
            times.append(t)
        avg_time = sum(times) / trials
        print(f"{name} (size {size}) took {avg_time:10.7f} seconds to run, on average")

def main():
    trials = 100
    list_sizes = [500, 1000, 5000]

    print("Insertion Sort")
    benchmark(insertion_sort, "Insertion Sort", list_sizes, trials)

    print("\nShell Sort")
    benchmark(shell_sort, "Shell Sort", list_sizes, trials)

    print("\nPython Built-in Sort")
    benchmark(python_sort, "Python Sort", list_sizes, trials)

if __name__ == "__main__":
    main()