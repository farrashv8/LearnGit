#Encrypt & Decrypt
import random
import string

character = " " + string.punctuation + string.digits + string.ascii_letters
character = list(character)
key = character.copy()
random.shuffle(key)

print(character)
print(key)

#Encrypt
text = input("Enter a message: ")
cipher_text = ""
for letter in text:
    index = character.index(letter)
    cipher_text += key[index]
print(f"your encrypted tect is : {cipher_text}")

#Decrypt
cipher_text = input("Enter an Encrypted code: ")
text = ""
for letter in cipher_text:
    index = key.index(letter)
    text += character[index]
print(f"your text is : {text}")

#Encrypt & Decrypt
#def your_text():
    #text = input("Enter a message: ")
    #cipher_text = ""
    #for letter in text:
        #index = character.index(letter)
        #cipher_text += key[index]
    #print(f"your encrypted tect is : {cipher_text}")
    #return cipher_text

#cipher_text = your_text()
#text = ""
#for letter in cipher_text:
    #index = key.index(letter)
    #text += character[index]
#print(f"your encrypted text is : {cipher_text}")
#print(f"your text is : {text}")