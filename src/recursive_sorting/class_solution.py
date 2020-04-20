def merge( arrA, arrB ):
    print(f"   MERGING: {arrA} - {arrB}")
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # Initialize pointers to the front of A and B arrays
    a = 0
    b = 0
    for i in range(elements):
        # Compare the first elements of A and B
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        # Copy the smallest to merged_arr
    return merged_arr
​
​
​
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    print(f"SORTING: {arr}")
    if len(arr) <= 1:
        return arr
    # Split the arrays into half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    # Sort each half
    left = merge_sort(left)
    right = merge_sort(right)
    # Merge them back together
    # return the array
    return merge(left, right)
​
