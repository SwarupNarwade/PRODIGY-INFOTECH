Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def caesar_cipher(text, shift, mode='encrypt'):
...     """
...     Encrypts or decrypts a given text using the Caesar Cipher.
... 
...     text: The input text to process.
...     shift: The number of positions to shift (positive for encryption, negative for decryption).
...     mode: 'encrypt' to encrypt, 'decrypt' to decrypt.
...     return: The processed text.
...     """
...     if mode == 'decrypt':
...         shift = -shift
... 
...     result = ""
...     for char in text:
...         if char.isalpha():
...             base = ord('A') if char.isupper() else ord('a')
...             new_char = chr((ord(char) - base + shift) % 26 + base)
...             result += new_char
...         else:
...             result += char
... 
...     return result
... 
... 
... # Main program
... if __name__ == "__main__":
...     print("Caesar Cipher Program")
...     mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
...     text = input("Enter the text: ").strip()
...     
...     while True:
...         try:
...             shift = int(input("Enter the shift value: ").strip())
...             break 
...         except ValueError:
...             print("Invalid input. Please enter a valid integer for the shift value.")

    result = caesar_cipher(text, shift, mode)
