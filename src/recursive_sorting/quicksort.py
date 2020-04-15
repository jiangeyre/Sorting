def quick_sort(arr):
    # Base case: arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    # Pick a pivot
    pivot = arr[0]
    # Separate all vals smaller and larger than the pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # Sort smaller and larger
    # Concatenate smaller + pivot + larger
    return quick_sort(smaller) + [pivot] + quick_sort(larger)


# MERGESORT
[2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
# (base case) If the array is empty or length 1, return
# Split the arrays into half
arr1 = [2, 0, 1, 3, 6]
arr2 = [9, 8, 5, 7, 4]
# Sort each half
arr1 = [0,1,2,3,6]
arr2 = [4,5,7,8,9]
# Merge them back together
# Compare the first values of each array, add smaller of the 2 to result
merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]