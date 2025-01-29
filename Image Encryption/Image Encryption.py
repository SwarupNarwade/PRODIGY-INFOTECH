Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
import numpy as np

print("Welcome to the Simple Image Encryption Tool.")

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save(output_path)
...     print(f"Image encrypted successfully. Encrypted image saved at: {output_path}")
... 
... def decrypt_image(encrypted_path, output_path, key):
...     encrypted_image = Image.open(encrypted_path)
...     encrypted_array = np.array(encrypted_image)
... 
...     decrypted_array = (encrypted_array - key) % 256
...     decrypted_image = Image.fromarray(np.uint8(decrypted_array))
...     decrypted_image.save(output_path)
...     print(f"Image decrypted successfully. Decrypted image saved at: {output_path}")
... 
... def main():
...     while True:
...         print("Type 'e' to encrypt an image, 'd' to decrypt an image, or 'q' to quit.")
...         choice = input("Your choice: ")
...         if choice == 'e':
...             image_path = input("Enter the path of the image to encrypt: ")
...             output_path = input("Enter the output path for the encrypted image: ")
...             key = int(input("Enter the encryption key (integer): "))
...             encrypt_image(image_path, output_path, key)
...         elif choice == 'd':
...             encrypted_path = input("Enter the path of the encrypted image: ")
...             output_path = input("Enter the output path for the decrypted image: ")
...             key = int(input("Enter the decryption key (same as encryption key): "))
...             decrypt_image(encrypted_path, output_path, key)
...         elif choice == 'q':
...             print("Exiting the program.")
...             break
...         else:
...             print("Invalid choice. Please try again.")
... 
... if __name__ == "__main__":
...     main()
