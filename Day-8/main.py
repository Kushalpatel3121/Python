"""Functions and Inputs"""

def greet():
    print("Hello World!\n"*3)

greet()

##Function that allows for input
def greet_with_name(name):
    print(f"Hello  {name}")

greet_with_name("Kushal")

##Functions with more than one params
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How is it in {location}?")

greet_with("Kushal","Surat")  


