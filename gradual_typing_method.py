import time

def gradual_typing(text):
    output = [' '] * len(text)
    
    for index, character in enumerate(text):
        if character.isalpha():
            for letter in range(ord('a'), ord(character.lower()) + 1):
                output[index] = chr(letter)
                print(''.join(output), end='\r')
                time.sleep(0.1)
        else:
            output[index] = character
            print(''.join(output), end='\r')
            time.sleep(0.1)
    
    print(''.join(output))


phrase = input("Please enter a text: ")
gradual_typing(phrase)

