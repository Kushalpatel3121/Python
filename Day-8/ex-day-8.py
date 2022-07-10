"""Ceasar Cipher"""
letters = ['a','b','c','d','e','f','j','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','j','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
text = input("Enter Text : \n").lower()
shift = int(input("Type shift number : "))

def encrypt(text,shift):
    message = ''
    for letter in text:
        position = letters.index(letter)
        new_position = position + shift
        message += letters[new_position]
    print(message)    

def decrypt(text,shift):
    message = ''
    for letter in text:
        position = letters.index(letter)
        old_position  = position - shift
        message += letters[old_position]
    print(message)

def caesar(text,shift,direction):
    end_text = ""
    for letter in text:
        position = letters.index(letter)
        if direction == 'decode':
            shift *= shift - 1
        new_position = position + shift
        end_text += letters[new_position]
    print(end_text)
if direction == 'encode':
    encrypt(text,shift)
elif direction =='decode':
    decrypt(text,shift)
else:
    print("Invalid Choice")

caesar(text,shift,direction)
