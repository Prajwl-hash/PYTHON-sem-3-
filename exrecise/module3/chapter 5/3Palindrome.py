<<<<<<< HEAD
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char .isalnum())
    return cleaned == cleaned [::-1]

input_string ="A man , a plan, a canal : Panama"
=======
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char .isalnum())
    return cleaned == cleaned [::-1]

input_string ="A man , a plan, a canal : Panama"
>>>>>>> c965dbf5152de176c2dbd9448cc71dbd01538425
print (is_palindrome(input_string))