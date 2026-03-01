def cocktail_sort(arr):
    n = len(arr)  # Get array length
    swapped = True  # Flag to track if swaps occurred
    start = 0  # Start of unsorted portion
    end = n - 1  # End of unsorted portion
    while swapped:  # Continue until no swaps
        swapped = False
        # Forward pass: bubble largest to end
        for i in range(start, end):
            if arr[i] > arr[i + 1]:  # If out of order
                # Swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:  # If sorted, break
            break
        end -= 1  # Shrink end (largest fixed)
        swapped = False
        # Backward pass: bubble smallest to start
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:  # If out of order
                # Swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1  # Shrink start (smallest fixed)
    return arr