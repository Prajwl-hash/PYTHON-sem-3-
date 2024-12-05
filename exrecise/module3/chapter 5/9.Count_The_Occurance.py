def character_count(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Example usage
input_string = "hello"
print(character_count(input_string))
