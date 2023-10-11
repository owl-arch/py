numbers = [1,2,3,4]
squared_numbers=[]

for num in numbers:
    squared_numbers.append(num ** 2)

print(f"squared_number = {squared_numbers}")

# Um jeito mais bacana de fazer

numbers = [1,2,3,4]
squared_numbers=[num ** 2 for num in numbers]

print(f"squared_number = {squared_numbers}")


##
# https://medium.com/@sarperismetmakas/python-for-and-while-loop-c72f660bb874
##
# Iterate over a dictionary and print its keys using a while loop
person_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
keys_list = list(person_dict.keys())
index = 0
while index < len(keys_list):
    print(keys_list[index])
    index += 1    