# Python program to find the ASCII value of a given character

# Get character input from the user

char = input("Enter a character: ")

# Check if the input is a single character

if len(char) == 1:

 ascii_value = ord(char)

 print(f"The ASCII value of '{char}' is {ascii_value}.")

else:

 print("Please enter only a single character.")