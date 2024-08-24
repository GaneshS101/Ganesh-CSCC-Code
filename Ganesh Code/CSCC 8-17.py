# Read the input numbers as a space-separated string
input_numbers = input()

# Convert the input string to a list of integers
numbers = list(map(int, input_numbers.split()))

# Filter out the negative integers
negative_numbers = [num for num in numbers if num < 0]

# Sort the negative integers in descending order
negative_numbers.sort(reverse=True)

# Output the sorted negative integers followed by a space
for num in negative_numbers:
    print(num, end=' ')