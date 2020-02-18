# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arr_a, arr_b ):
    elements = len( arr_a ) + len( arr_b )
    merged_arr = []#[0] * elements
    # TO-DO

    #short_arr_len = len(arr_a) if len( arr_a ) < len( arr_b ) else len(arr_b)
    
    arr_a_idx = 0
    arr_b_idx = 0

    while arr_a_idx < len(arr_a) and arr_b_idx < len(arr_b):
        print(arr_a_idx, arr_b_idx)
        if arr_a[arr_a_idx] < arr_b[arr_b_idx]:
            merged_arr.append(arr_a[arr_a_idx])
            arr_a_idx += 1
        elif arr_a[arr_a_idx] > arr_b[arr_b_idx]:
            merged_arr.append(arr_b[arr_b_idx])
            arr_b_idx += 1
        else:
#            merged_arr[arr_a_idx], merged_arr[arr_a_idx + 1] = arr_a[arr_a_idx], arr_a[arr_a_idx]
            merged_arr += [arr_a[arr_a_idx], arr_a[arr_a_idx]]
            arr_a_idx += 1
            arr_b_idx += 1

    if(arr_a_idx == len(arr_a)):
        merged_arr += arr_b[arr_b_idx:]
    else:
        merged_arr += arr_a[arr_a_idx:]
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) == 1:
        return arr

    middle_ele = int(len(arr) / 2)

    arr1 = merge_sort(arr[0:middle_ele])
    arr2 = merge_sort(arr[middle_ele:])

    return merge(arr1, arr2)



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
