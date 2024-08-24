word = input()
password = ''
replacement_key = {
    'a': '@', 'A': '@',
    'm': 'M',
    'i': '1', 'I': '1',
    'b': '8', 'B': '8',
    's': '$', 'S': '$'
}

# Replace characters using the replacement key
for char in word:
    password += replacement_key.get(char, char)  # Replace or keep the original character

# Append '!' to the end of the password
password += '!'

# Output the stronger password
print(password)