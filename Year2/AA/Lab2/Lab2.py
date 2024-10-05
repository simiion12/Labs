import time
import matplotlib.pyplot as plt
import random


class Algorithms:
    def __init__(self, random_list):
        self.random_list = random_list

    def quickSort(self):
        # Checking if the list is empty or has only one element
        if len(self.random_list) <= 1:
            return self.random_list
        else:
            # Choosing the pivot
            pivot = self.random_list[0]
            # Creating list which has elements less than or equal to the pivot
            less = [i for i in self.random_list[1:] if i <= pivot]
            # Creating list which has elements greater than the pivot
            greater = [i for i in self.random_list[1:] if i > pivot]
            # Recursively calling the quickSort function for the less and greater lists
            return Algorithms(less).quickSort() + [pivot] + Algorithms(greater).quickSort()

    def mergeSort(self):
        # Checking if the list is empty or has only one element
        if len(self.random_list) <= 1:
            return self.random_list

        # Splitting the array into two halves
        mid = len(self.random_list) // 2
        left_half = self.random_list[:mid]
        right_half = self.random_list[mid:]

        # Recursively calling mergeSort on both halves
        left_half = Algorithms(left_half).mergeSort()
        right_half = Algorithms(right_half).mergeSort()

        # Merging the sorted halves
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        # Creating an empty list to store the merged elements
        merged = []
        left_index = right_index = 0

        # While loop that continues until either
        # the left array and the right array is fully processed.
        while left_index < len(left) and right_index < len(right):
            # This block compares the elements at the current
            # positions in the left and right arrays
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Append the remaining elements from the left and right halves
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

    def heapSort(self):
        n = len(self.random_list)

        # This loop is responsible for creating a max-heap from the input list.
        # It starts from the last non-leaf node and iterates backwards to the root node
        # In each iteration, it calls the heapify method to ensure that the subtree rooted
        # at index i satisfies the max-heap property.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.random_list, n, i)

        # This loop extracts elements from the max-heap one by one.
        # It starts from the end of the heap and moves towards the beginning.
        # In each iteration, it swaps the root of the heap (located at index 0)
        # with the last element of the heap (located at index i), effectively removing
        # the maximum element from the heap
        for i in range(n - 1, 0, -1):
            self.random_list[i], self.random_list[0] = self.random_list[0], self.random_list[i]  # Swap
            # After the swap, it calls the heapify method to restore the max-heap property
            # in the remaining heap elements.
            self.heapify(self.random_list, i, 0)

        return self.random_list

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than the parent
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not the root, swap it with the root and heapify the affected subtree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify(arr, n, largest)

    def selectionSort(self, ascending=True):
        n = len(self.random_list)
        swaps = 0
        comparisons = 0

        # Helper function to swap elements and update swap count
        def swap(arr, i, j):
            nonlocal swaps
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

        # Helper function to compare elements and update comparison count
        def compare(a, b):
            nonlocal comparisons
            comparisons += 1
            if ascending:
                return a < b
            else:
                return a > b
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if compare(self.random_list[j], self.random_list[min_index]):
                    min_index = j
            if min_index != i:
                swap(self.random_list, i, min_index)
        return self.random_list

    def introSort(self):
        # Determine the minimum size of a run
        min_run = 32

        # Get the length of the list
        n = len(self.random_list)

        # Define the insertion sort function
        def insertion_sort(arr, left, right):
            for i in range(left + 1, right + 1):
                key = arr[i]
                j = i - 1
                while j >= left and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        # Define the merge function
        def merge(arr, left, mid, right):
            len1, len2 = mid - left + 1, right - mid
            left_arr, right_arr = [], []

            # Copy data to temporary arrays
            for i in range(len1):
                left_arr.append(arr[left + i])
            for i in range(len2):
                right_arr.append(arr[mid + 1 + i])

            # Merge the temporary arrays back into arr
            i = j = 0
            k = left
            while i < len1 and j < len2:
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            # Copy the remaining elements of left_arr[], if any
            while i < len1:
                arr[k] = left_arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of right_arr[], if any
            while j < len2:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        # Sort the array using insertion sort for small runs
        for i in range(0, n, min_run):
            insertion_sort(self.random_list, i, min((i + min_run - 1), (n - 1)))

        # Merge the runs using merge sort
        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min((left + size - 1), (n - 1))
                right = min((left + 2 * size - 1), (n - 1))
                merge(self.random_list, left, mid, right)
            size *= 2

        return self.random_list

    def timsort(self):
        return self.introSort()

quickSort_time, mergeSort_time, heapSort_time, selectionSort_time, insertionSort_time, timSort_time = [], [], [], [], [], []

# Loop to perform each algorithm on the different list sizes
for i in range(1, 5):
    # List for testing algorithms
    random_list_1000000 = [random.random() for i in range(1000000)]
    random_list_100000 = [random.random() for i in range(100000)]
    random_list_10000 = [random.random() for i in range(10000)]
    random_list_1000 = [random.random() for i in range(1000)]
    random_list_100 = [random.random() for i in range(100)]
    if i == 1:
        start = time.perf_counter()
        Algorithms(random_list_100).quickSort()
        quickSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_100).mergeSort()
        mergeSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_100).heapSort()
        heapSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_100).selectionSort()
        selectionSort_time.append(time.perf_counter() - start)
        Algorithms(random_list_100).timsort()
        timSort_time.append(time.perf_counter() - start)
    elif i == 2:
        start = time.perf_counter()
        Algorithms(random_list_1000).quickSort()
        quickSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_1000).mergeSort()
        mergeSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_1000).heapSort()
        heapSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_1000).selectionSort()
        selectionSort_time.append(time.perf_counter() - start)
        Algorithms(random_list_1000).timsort()
        timSort_time.append(time.perf_counter() - start)
    elif i == 3:
        start = time.perf_counter()
        Algorithms(random_list_10000).quickSort()
        quickSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_10000).mergeSort()
        mergeSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_10000).heapSort()
        heapSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_10000).selectionSort()
        selectionSort_time.append(time.perf_counter() - start)
        Algorithms(random_list_10000).timsort()
        timSort_time.append(time.perf_counter() - start)
    elif i == 4:
        start = time.perf_counter()
        Algorithms(random_list_100000).quickSort()
        quickSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_100000).mergeSort()
        mergeSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_100000).heapSort()
        heapSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_100000).selectionSort()
        selectionSort_time.append(time.perf_counter() - start)
        Algorithms(random_list_100000).timsort()
        timSort_time.append(time.perf_counter() - start)
    elif i == 5:
        start = time.perf_counter()
        Algorithms(random_list_1000000).quickSort()
        quickSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_1000000).mergeSort()
        mergeSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_1000000).heapSort()
        heapSort_time.append(time.perf_counter() - start)
        start = time.perf_counter()
        Algorithms(random_list_1000000).selectionSort()
        selectionSort_time.append(time.perf_counter() - start)
        Algorithms(random_list_1000000).timsort()
        timSort_time.append(time.perf_counter() - start)

# Plotting the results
x = [100, 1000, 10000, 100000, 1000000]
y = [quickSort_time, mergeSort_time, heapSort_time, selectionSort_time, timSort_time]
labels = ['Quick Sort', 'Merge Sort', 'Heap Sort', 'Selection Sort', 'Tim Sort']
for i in range(len(y)):
    plt.plot(x, y[i])
    plt.scatter(x, y[i])
    plt.xlabel('List Size')
    plt.ylabel('Time (s)')
    plt.title(labels[i])
    plt.show()

# Plotting the results in a single graph
for i in range(len(y)):
    plt.figure(1, figsize=(10, 5))
    plt.plot(x, y[i], label=labels[i])
    plt.scatter(x, y[i])
    if i % 2 == 0:
        for j, txt in enumerate(y[i]):
            plt.text(x[j], y[i][j], "{:.5f}".format(txt), ha='left')

plt.xscale('log')
plt.yscale('log')
plt.title('Sorting Algorithms Performance')
plt.xlabel('List Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()

# Data
quickSort_time = [0.00021740001102443784, 0.0021785999997518957, 0.02680839999811724, 0.3480222999933176, 5.744825900008436, 97.0298874]
mergeSort_time = [0.0002535999956307933, 0.0029111000039847568, 0.035978500003693625, 0.4342802000028314, 7.269950300003984, 134.26969610000378]
heapSort_time = [0.000361100013833493, 0.005885100006707944, 0.1048605999967549, 0.634930300002452, 15.85307680000551, 271.1590465000045]
timSort_time = [0.00014589997590519488, 0.002057200006674975, 0.030239199986681342, 0.4507247000001371, 5.845877099985955, 84.21573450000142]
selectionSort_time = [0.0009512999968137592, 0.08513389999279752, 9.029996199999005, 1864.5088115999824, 0, 0]
