x = int(input())

# Convert the integer to a binary string, remove the '0b' prefix
binary_str = bin(x)[2:]

# Reverse the binary string
reversed_binary_str = binary_str[::-1]

# Output the reversed binary string
print(reversed_binary_str)
