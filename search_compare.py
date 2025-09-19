import time
import random

# Sequential Search: Goes through the list one element at a time until it finds the target or reaches the end. Works on unsorted lists.
def sequential_search (alist, item):
    pos = 0
    found = False
    # Loop through list until item found or end reached
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

# Ordered Sequential Search: Assumes the list is sorted. Stops early if the current element is greater than the target, since it knows the target cannot appear later in the sorted list.
def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop: 
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
        pos += 1
    return found

# Iterative Binary Search: Assumes the list is sorted. Repeatedly cuts the list in half, checking the middle element and then deciding whether to search the left or right half. Continues until the item is found or the search space is empty.
def binary_search_iterative(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item <alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

# Recursive Binary Search: Works the same as iterative binary search, but instead of looping, it calls itself recursively on the left or right half of the list.
def binary_search_recursive (alist, item, first=0, last=None):
    if last is None:
        last = len(alist) - 1
    if first > last:
        return False
    midpoint = (first+last)//2
    if alist[midpoint]==item:
        return True
    elif item <alist[midpoint]:
        return binary_search_recursive(alist, item, first, midpoint - 1)
    else:
        return binary_search_recursive(alist, item, midpoint + 1, last)

def time_function (func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end-start

def benchmark( func, name, list_sizes, trials = 100):
    for size in list_sizes:
        times = []
        for _ in range(trials):
            alist = [random.randint(1, size * 10) for _ in range(size)]
            if func in (ordered_sequential_search, binary_search_iterative, binary_search_recursive):
                alist.sort()
            target = 99999999
            _, t = time_function(func, alist, target)
            times.append(t)
        avg_time = sum(times) / trials
        print(f"{name} (size {size}) took {avg_time:10.7f} seconds to run, on average")

def main():
    trials = 100
    list_sizes = [500, 1000, 5000]

    print("Sequential Search")
    benchmark(sequential_search, "Sequential Search", list_sizes, trials)

    print("\nOrdered Sequential Search")
    benchmark(ordered_sequential_search, "Ordered Sequential Search", list_sizes, trials)

    print("\nIterative Binary Search")
    benchmark(binary_search_iterative, "Iterative Binary Search", list_sizes, trials)

    print("\nRecursive Binary Search")
    benchmark(binary_search_recursive, "Recursive Binary Search", list_sizes, trials)

if __name__ == "__main__":
    main()