def calculate_total_distance(left_list, right_list):
    """
    Calculate the total distance between corresponding elements
    of two sorted lists.
    """
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

# Read input data from file
try:
    with open("/home/runner/adventofcode2024/input.txt", "r") as f:

        lines = [[int(i) for i in line.split()] for line in f]
except FileNotFoundError:
    print("Error: File not found. Please ensure the input file is in the correct path.")
    exit()

# Split the data into two lists
left_list, right_list = zip(*lines)

# Part 1: Calculate the sum of absolute differences
sorted_left, sorted_right = sorted(left_list), sorted(right_list)
absolute_difference_sum = sum(abs(a - b) for a, b in zip(sorted_left, sorted_right))
print("Sum of Absolute Differences:", absolute_difference_sum)

# Part 2: Calculate the total distance using the function
total_distance = calculate_total_distance(left_list, right_list)
print("Total Distance:", total_distance)
