# Get the input from the user
sentence = input("Enter a sentence: ")

# Initialize a counter for alphabetic characters
count = 0

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is alphabetic (A-Z or a-z)
    if char.isalpha():
        count += 1

# Print the number of alphabetic characters
print("Number of alphabetic characters:", count)
