# dictionary
# a data collection which works based on key-value pair mechanism contains item(s)


# key : an unique identity which is part of item (left portion), there will not be any duplicates in keys.
# value : a non-unique identity which is part of item (right portion), there may/may not duplicates
# item = key+value
# eg: "30724": "Bharath"

# adhar and name dictionary.
# Eg: {"30724": "Bharath", 30725": "Avinash",30726": "Visu",30727": "Avinash", }

# empty dictionary with flower brackets
# dict_1 = {}
dict_1 = {"30724": "Bharath", "30725" :"Avinash","30726": "Visu","30727": "Avinash"}
print(dict_1)

# empty dictionary with dict built in method
# dict_2 = dict()
dict_2 = dict({"30724": "Bharath", "30725" :"Avinash","30726": "Visu","30727": "Avinash"})
print(dict_2)

# creating dictionary with list and tuple
dict_3 = dict([("30724", "Bharath"),("30725","Avinash"),("30726","Visu"),("30727","Avinash")])
print(dict_3)

# Adding an SINGLE item to dictionary
dict_3["30728"]= "Raviteja"
print(dict_3)


# overrriding the existing/replacing value for key "30728"
dict_3["30728"]= "Raviteja1"
print(dict_3)

# Adding an MULTIPLE values to a same key  in a  dictionary will create tuple of values.
dict_3["30728"]= "Niramla", "Vamsi"
print(dict_3)

# dictionary mutable
dict_3["30728"]= "Raviteja Pamujula"
print(dict_3)

# printing value based on key value
print(dict_3["30725"])

print("________________________________________________________________________________________________________________________")
# Accessing all keys
print(dict_3.keys())
print(type(dict_3.keys()))
# dict_keys(['30724', '30725', '30726', '30727', '30728'])
# <class 'dict_keys'>

# converting into list
dict_3_keys_list = list(dict_3.keys())
print(dict_3_keys_list)
# ['30724', '30725', '30726', '30727', '30728']

# Accessing all values
print(dict_3.values())
print(type(dict_3.values()))
# dict_values(['Bharath', 'Avinash', 'Visu', 'Avinash', 'Raviteja Pamujula'])
# <class 'dict_values'>

# converting into list
dict_3_values_list = list(dict_3.values())
print(dict_3_values_list)
# ['Bharath', 'Avinash', 'Visu', 'Avinash', 'Raviteja Pamujula']

# Accessing all items
print(dict_3.items())
print(type(dict_3.items()))
# dict_items([('30724', 'Bharath'), ('30725', 'Avinash'), ('30726', 'Visu'), ('30727', 'Avinash'), ('30728', 'Raviteja Pamujula')])
# <class 'dict_items'

dict_3_items_list = list(dict_3.items())
print(dict_3_items_list)
# [('30724', 'Bharath'), ('30725', 'Avinash'), ('30726', 'Visu'), ('30727', 'Avinash'), ('30728', 'Raviteja Pamujula')]


# checking non existing things
# print(dict_3[2415])
# KeyError: 2415

dict_4 = {"30724": "Bharath", "30725" :"Avinash","30726": "Visu","30727": "Avinash", "30724":"Vishnu"}
print(dict_4)
# pop method gives value for the key provided
print(dict_4.get("30725"))
# it will override/replace the value if you give different value to the same key.
print("________________________________________________________________________________________________________________________")

print(dict_4)
print(dict_4.pop("30725"))

print(dict_4)
# popitem gives tuple of key and value
print(dict_4.popitem())

print(dict_4)
# clears
dict_4.clear()
print(dict_4)

