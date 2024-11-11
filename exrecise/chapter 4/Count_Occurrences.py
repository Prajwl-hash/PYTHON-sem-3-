fruits = ["apple", "banana", "apple", "orange", "banana"]
fruit_count = {fruit: fruits.count(fruit) for fruit in set(fruits)}
print(fruit_count)
