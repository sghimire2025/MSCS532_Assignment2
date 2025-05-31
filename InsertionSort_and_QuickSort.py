import time
import tracemalloc
import random


# fn to generate random data
def generateData(size):
    return {
        "Sorted Data": list(range(size)),
        "Reverse Sorted Data": list(range(size, 0, -1)),
        "Random Data": [random.randint(0, size) for _ in range(size)],
    }


# Different dataset sizes
sizes = [100, 1000]

#insertion sort
def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums



# Print out the algorithm performance
def printAnalysis(sortingFunction, dataset, algorithm, datasetLabel):
    tracemalloc.start()
    start = time.perf_counter()
    sortingFunction(dataset.copy())
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_ms = round((end - start) * 1000, 3)
    mem_kb = peak // 1024
    print(f"{algorithm} on {datasetLabel}: Time = {time_ms} ms | Memory usage = {mem_kb} KB")




print("Comparing Insertion Sort and Quick Sort\n")
for size in sizes:
   
    datasets = generateData(size)
    
    for label, data in datasets.items():
        printAnalysis(insertionSort, data, "Insertion Sort", label)
       # printAnalysis - quick
