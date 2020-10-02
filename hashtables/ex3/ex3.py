# A list of lists that contain integers
# Find the number(s) that exist in all lists

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    # Get each value
    for array in arrays:
        for value in array:
            # Append each value to cache
            if value not in cache:
                cache[value] = 1
            else:
                cache[value] += 1
    
    # Loop through cache
    for key, value in cache.items():
        # Push value to list if it occurs multiple times
        if value > 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
