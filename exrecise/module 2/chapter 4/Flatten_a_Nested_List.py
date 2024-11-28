from contourpy.util import data
from numpy import maximum

nested_list = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

# Assuming 'data' is defined somewhere in the code
print(data["person"]["details"]["city"])  # Output: New York
print(maximum)
