import keyboard

# Define the key mapping
key_map = {
    'a': '\U+2009'
}

# Function to handle key press
def handle_key_press(e):
    if e.name in key_map:
        keyboard.press_and_release(key_map[e.name])
        e.suppress = True  # Suppress the original key press
    elif e.name == '1':
        # Stop the script when '1' is pressed
        keyboard.unhook_all()
        quit()

# Hook key press event
keyboard.hook_key('a', handle_key_press)
keyboard.hook_key('1', handle_key_press)

# Block the script from exiting
keyboard.wait()