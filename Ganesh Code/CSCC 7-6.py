while True:
    # Read input from the user
    user_input = input()
    
    # Split the input into the word and the integer
    word, num = user_input.split()
    
    # Check if the input string is 'quit'
    if word == "quit":
        break
    
    # Convert the num to an integer
    num = int(num)
    
    # Output the sentence using the input values
    print(f"Eating {num} {word} a day keeps you happy and healthy.")
