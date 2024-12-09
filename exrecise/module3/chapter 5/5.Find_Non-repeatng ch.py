<<<<<<< HEAD
def first_non_repeating(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None

# Example usage
input_string = "swiss"
print(first_non_repeating(input_string))
=======
def first_non_repeating(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None

# Example usage
input_string = "swiss"
print(first_non_repeating(input_string))
>>>>>>> c965dbf5152de176c2dbd9448cc71dbd01538425
