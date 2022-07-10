"""Dictionaries and Nesting"""

##Values in Dictionaries are known by their keys
programming_dictionary = {
    "Bug":"An error in a program",
    "Loop":"The action of doing something again and again"
    }

print(programming_dictionary["Bug"])
print(programming_dictionary["Loop"])

# Adding item in dictionary
programming_dictionary["Function"] = "A piece of code that perform specific action"

print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe the dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through the dictionary
for item in programming_dictionary:
    print(item)     ##Prints only keys


# NESTING
travel_log = {
    "Germany" : ["Berlin","Stuttgart","Hamburg"],    # Here Value of the key is a list
    "France" : {
        "Cities_visited":["Paris","Dijon"],
        "Food_eaten" : "Bread",
        "total_visits" : 1
    }
}

#Nesting a dictionary in a list
travel_log = [
    {"Country":"Germany","cities_visited":["Berlin","Hamburg"],"total_visits":1},    # Here Value of the key is a list
    {"Country":"France","cities_visited":["Paris","Dijon","Lille"],"total_visits":1}
]