def swap_tuple(t):
    return (t[-1],) + t[1:-1] + (t[0],)

my_tuple = (1, 2, 3, 4, 5)
swapped = swap_tuple(my_tuple)
print(swapped)
