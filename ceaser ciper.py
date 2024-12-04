import string
lower_case = string.ascii_lowercase
alphabets = list(lower_case)
logo = """           
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

def encrypt(original_text, shift_amount):
        final_text = ""
        for letters in original_text:
            if letters not in alphabets:
                final_text += letters
            else:
                shifted_index = alphabets.index(letters) + shift_amount
                shifted_index %= len(alphabets)
                final_text += alphabets[shifted_index]
        return final_text

def decode(shifted_text,shift_amount):
        original_text = ""
        for letters in shifted_text:
            if letters not in alphabets:
                original_text += letters
            else:
                original_index = alphabets.index(letters) - shift_amount
                original_index %= len(alphabets)
                original_text += alphabets[original_index]
        return original_text
def ceaser(my_text,encode_or_decode):
    encoded_text = encrypt(my_text, shift_number)
    decoded_text = decode(encoded_text, shift_number)
    if encode_or_decode == "encode":
        print(f"the encoded text :{encoded_text}")

    if encode_or_decode == "decode":
        print(f"the decoded text:{decoded_text}")
print(logo)
text = input("Type your text:").lower()
should_continue = True
while should_continue:
    direction = input("Type 'encode' for encoded letters and type 'decode' for decoded letters").lower()
    shift_number = int(input("the shift number:"))
    ceaser(text,direction)
    consent = input("Type 'yes' if to continue or type 'no' to exit").lower()
    if consent == "no":
        should_continue = False
        print("Good bye")