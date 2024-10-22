# Python Dictionaries

my_dictionary = {
    "school": "Valencia",
    "color": "red",
    "major": "basket weaving",
    "grad": 2024,
}

x = my_dictionary["grad"]
y = my_dictionary.get("school")
print(x)
print(y)

my_keys = my_dictionary.keys()
print(my_keys)

my_dictionary['school'] = 'Seminole State'
print(my_dictionary["school"])

my_values = my_dictionary.values()
print(my_values)

my_dictionary.update({'school': "Valencia"})
print(my_dictionary["school"])

my_dictionary.pop("major")
print(my_dictionary)

del my_dictionary["grad"]
print(my_dictionary)

#file operation for Python. a means append
f = open("test.txt", "a")
f.write("Hello, Valencia Class")
f.close()

# r means to read the file
f = open("test.txt", "r")
print(f.read())
f.close()