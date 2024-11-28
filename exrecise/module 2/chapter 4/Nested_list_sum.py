nested_list = [[1, 2], [3, 4], [5, 6]]
total = sum(sum(sublist) for sublist in nested_list)
print(total)
