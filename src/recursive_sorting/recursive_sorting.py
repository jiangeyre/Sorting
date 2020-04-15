# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # index iterations for each arr
    a, b, c = 0, 0, 0
    # compare and sort the elements of both of the arrays to a merged array
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            c = c + 1
            a = a + 1
        else:
            merged_arr[c] = arrB[b]
            c = c + 1
            b = b + 1
    # remaining elements need to be added to the merged arr
    while a < len(arrA):
        merged_arr[c] = arrA[a]
        c = c + 1
        a = a + 1
    while b < len(arrB):
        merged_arr[c] = arrB[b]
        c = c + 1
        b = b + 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # establish a base case
    if len(arr) <= 1:
        return arr
    # divide until single element arrays
    mid = len(arr) // 2
    l = merge_sort(arr[mid:])
    r = merge_sort(arr[:mid])
    # compare values and sort the arrays
    arr = merge(l, r)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
