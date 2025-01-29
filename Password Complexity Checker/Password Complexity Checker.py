Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def check_password_complexity(password):
...     length_error = len(password) < 8
...     digit_error = re.search(r"\d", password) is None
...     uppercase_error = re.search(r"[A-Z]", password) is None
...     lowercase_error = re.search(r"[a-z]", password) is None
...     symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
... 
...     errors = {
...         "length": length_error,
...         "digit": digit_error,
...         "uppercase": uppercase_error,
...         "lowercase": lowercase_error,
...         "symbol": symbol_error
...     }
... 
...     return errors
... 
... def password_strength(password):
...     errors = check_password_complexity(password)
... 
...     if all(not error for error in errors.values()):
...         return "Strong"
...     elif sum(errors.values()) == 1:
...         return "Moderate"
...     else:
...         return "Weak"
... 
... def main():
...     print("Password Complexity Checker")
...     while True:
...         password = input("Enter a password to check (or type 'exit' to quit): ")
...         if password.lower() == 'exit':
...             print("Exiting the Password Complexity Checker.")
...             break
...         
        strength = password_strength(password)
        print(f"Password strength: {strength}")
        errors = check_password_complexity(password)
        if strength != "Strong":
            print("Issues:")
            if errors["length"]:
                print("- Password must be at least 8 characters long.")
            if errors["digit"]:
                print("- Password must contain at least one digit.")
            if errors["uppercase"]:
                print("- Password must contain at least one uppercase letter.")
            if errors["lowercase"]:
                print("- Password must contain at least one lowercase letter.")
            if errors["symbol"]:
                print("- Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

if __name__ == "__main__":
    main()
