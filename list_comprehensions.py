# List of names
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
# List of full names
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# List of almost numbers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# List comprehension to create a list of integers from the above list of strings
numbers = [int(num) for num in almost_numbers]
print(numbers)

# List comprehension to create a list of only the numbers that are greater than 9 from the numbers
numbers_greater_than_9 = [num for num in numbers if num > 9]
print(numbers_greater_than_9)

# List comprehension and the join string method to create a string of the last names
# for those full names longer than 11 characters
long_full_names_last_names = ', '.join([name.split()[1] for name in full_names if len(name) > 11])
print(long_full_names_last_names)
