# Given a list of integers:
# Find the positive integers that have corresponding negative integers

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []

    # Make a dict from the list
    num_dict = {num: True for num in a}

    # Loop through 'a'
    for num in a:
        # The number must be positive and have a corresponding negative value
        if num > 0 and (num * -1) in num_dict:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
