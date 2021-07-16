alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(pure_text, shift_amount):
    encoded = ""
    for letter in pure_text:
        index = alphabet.index(letter)
        new_position = index + shift_amount
        if new_position > 25:
            new_position -= 26
        encoded += alphabet[new_position]
    print(f"The encoded text is '{encoded}'")
    
encrypt(text, shift)

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 