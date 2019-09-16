my_list = ["strings", 15, 15.6, True]

my_list.append(6)
my_list.insert(1, "insert")

my_list.remove(15)

#print(my_list)

last_value = my_list.pop()

#print(my_list[1])
#print(my_list)

#print(last_value)

my_list_of_numbers = [1, 9, 22, 6, 8, 65, 14, 99]
my_list_of_numbers_two = [22, 23]

#my_list_of_numbers.sort
#my_list_of_numbers.sort(reverse = True)
my_list_of_numbers.extend(my_list_of_numbers_two)

print(my_list_of_numbers)
