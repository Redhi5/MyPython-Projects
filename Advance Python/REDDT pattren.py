def print_reddy_pattern():
    # Define the pattern for each letter
    pattern = {
        'R': ["R R R", "R  R ", "RRR  ", "R  R ", "R   R"],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
    }
    
    # Get the list of letters in "REDDY"
    letters = "REDDY"
    
    # Print each row of the pattern
    for i in range(5):  # Number of rows in each letter pattern
        for letter in letters:
            print(pattern[letter][i], end="  ")  # Print each letter's row with spacing
        print()  # New line after each row

# Call the function to print the pattern
print_reddy_pattern()
