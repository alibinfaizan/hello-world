# SUM OF ALL THE ELEMENTS IN A LIST

my_list = [3, 6, 5, 4, 3]
sum = sum(my_list)
print(sum)

# LARGEST ELEMENT OF A LIST

my_list = [3, 6, 5, 4, 3]
largest = max(my_list)
print(largest)

# SMALLEST ELEMENT OF A LIST

my_list = [3, 6, 5, 4, 3]
smallest = min(my_list)
print(smallest)

# SORTED LIST IN ASCENDING ORDER

my_list = [3, 6, 5, 4, 3]
asc = sorted(my_list)
print(asc)

# SORTED LIST IN DESCENDING ORDER

my_list = [3, 6, 5, 4, 3]
des = sorted(my_list, reverse=True)
print(des)


# SPECIAL CONDITIONS ON LISTS

l = [0, 0, 1, 5, 9]
print(all(l)) # >>> False : Since there are some zeros in the list
print(any(l)) # >>> True : Since there are some non-zero elements in the list
