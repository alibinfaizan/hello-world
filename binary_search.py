def b_search(arr, key, low high):
    if low > high:
        return "Number Not Found!"
    else:
        mid = (low + high) // 2
        if key==arr[mid]:
            return "Number Found!"
        elif key < arr[mid]:
            return b_search(arr, key, low mid-1)
        else:
            return b_search(arr, key, mid+1, high)
