def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
           
            result += char

    return result
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)
# Test cases
print("caesar ciphering:")
print("Hello, World!")         
print(caesar_cipher("Hello, World!", 5))  

print()

print("caesar deciphering:")
encoded = caesar_cipher("Attack at dawn!", 5)
print(encoded)                     # Fyyfhp fy ifbs!
print(caesar_decipher(encoded, 5)) # Attack at dawn!