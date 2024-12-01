# Function to calculate the total distance (Part 1)
def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate distances
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

# Function to calculate the similarity score (Part 2)
def calculate_similarity_score(left_list, right_list):
    # Create a dictionary to count occurrences in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate the similarity score
    similarity_score = sum(num * right_counts.get(num, 0) for num in left_list)
    return similarity_score

# Read the input from the file
try:
    with open("input.txt", "r") as file:
        # Parse input into two separate lists
        left_list = []
        right_list = []
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Calculate and print results for both parts
    total_distance = calculate_total_distance(left_list, right_list)
    print("Total Distance (Part 1):", total_distance)

    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score (Part 2):", similarity_score)

except FileNotFoundError:
    print("Error: The input file 'input.txt' was not found.")
except ValueError:
    print("Error: The input file 'input.txt' contains invalid data.")
