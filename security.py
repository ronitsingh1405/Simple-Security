alphabets = 'abcdefghijklmnopqrstuvwxyz'
key = 4
encrypted_word = ''

input_word = input("Enter the word to be encrypted : ")

for char in input_word:
    position = alphabets.find(char)
    new_position = (position-key)%26
    new_char = alphabets[new_position]
    print(f"The encrypted character is : {new_char}")
    encrypted_word += new_char

print("")    
print(f"Entered word is : {input_word}")
print(f"The encrypted word is : {encrypted_word}")
