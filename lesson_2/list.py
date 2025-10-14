
# List datatype 
my_friends = ['John', 'Musa', 'Tolu', 'Jummai','Seun']

# dictionary datatype
students = {
    'name': 'John',
    'age': 20,
    'is_student': True,
    'courses': ['Math', 'CompSci'], 
    'address': {
        'street': '123 Main St',
        'city': 'Lagos',
        'state': 'Lagos'
    },
    'tribe': 'Yoruba'
}



# print(f" My friends is: {my_friends[0]} and my only female is {my_friends[3]}")
print(f" My name is {students['name']} and I am {students['age']} years old. I am from the {students['tribe']} tribe and my address is {students['address']['street']}, {students['address']['city']}, {students['address']['state']}. I study {students['courses'][0]} and {students['courses'][1]}") 