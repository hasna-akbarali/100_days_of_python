caesar_cipher_logo = logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def encode(word, shift):
    output_word = ''
    for letter in word:
            output_word = output_word + chr(int(ord(letter))+shift)
    print(f'Here is the encoded result: {output_word}')
        
def decode(word, shift):
    output_word = ''
    for letter in word:
            output_word = output_word + chr(ord(letter)-shift)
    print(f'Here is the decoded result: {output_word}')
        
def encode_or_decode() :
    user_choice = input('Type \'encode\' to encrypt and \'decode\' to decrypt :')
    word = input('Type your message: \n')
    shift = int(input('Type your shift number: \n'))

    if user_choice == 'encode' :
        encode(word,shift)
        
    elif user_choice == 'decode' :
        decode(word,shift)
    else:
        print('Please enter a valid choice!')
    again = input('Type \'yes\' if you want to go again. Otherwise type \'no\'. \n').lower()
    if(again == 'yes'):
        encode_or_decode()

print(caesar_cipher_logo)        
encode_or_decode()
