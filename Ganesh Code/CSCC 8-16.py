# Read the input numbers as a space-separated string
input_numbers = input()

# Convert the input string to a list of floats
numbers = list(map(float, input_numbers.split()))

if numbers:
    # Calculate the maximum and average of the numbers
    max_number = max(numbers)
    average = sum(numbers) / len(numbers)

    # Output the results formatted to two decimal places
    print(f"{max_number:.2f} {average:.2f}")