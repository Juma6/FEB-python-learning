my_list = []
my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

print(my_list)  # Output the sorted list

index_of_60 = my_list.index(60)  # Find the index of the value 60
print(f"The index of 60 is: {index_of_60}")