import os
import re
import time


def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None


def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string



# key events like receive call, stop call, go back
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')
# import os
# import re
# import time

# # Extract YouTube search term from a command
# def extract_yt_term(command):
#     """
#     Extract a YouTube search term from the user's command.
#     :param command: The command spoken by the user (e.g., "Play some music on YouTube").
#     :return: The extracted term to search for on YouTube, or None if no match is found.
#     """
#     # Define a regular expression pattern to capture the song name
#     pattern = r'play\s+(.*?)\s+on\s+youtube'
#     # Use re.search to find the match in the command
#     match = re.search(pattern, command, re.IGNORECASE)
#     # If a match is found, return the extracted song name; otherwise, return None
#     return match.group(1) if match else None


# # Remove unwanted words from a string
# def remove_words(input_string, words_to_remove):
#     """
#     Remove specific words from the input string.
#     :param input_string: The input string containing words.
#     :param words_to_remove: A list of words to be removed from the input string.
#     :return: A string with the specified words removed.
#     """
#     # Split the input string into words
#     words = input_string.split()

#     # Remove unwanted words
#     filtered_words = [word for word in words if word.lower() not in words_to_remove]

#     # Join the remaining words back into a string
#     result_string = ' '.join(filtered_words)

#     return result_string


# # Key events like receiving a call, stopping a call, or going back
# def keyEvent(key_code):
#     """
#     Simulate key events on an Android device using ADB.
#     :param key_code: The keycode to simulate (e.g., 5 for receiving a call, 6 for ending a call).
#     """
#     command = f'adb shell input keyevent {key_code}'
#     os.system(command)
#     time.sleep(1)  # Small delay after executing the command


# # Tap event used to tap anywhere on the screen
# def tapEvents(x, y):
#     """
#     Simulate a tap on the Android device at specific coordinates.
#     :param x: The X-coordinate of the tap.
#     :param y: The Y-coordinate of the tap.
#     """
#     command = f'adb shell input tap {x} {y}'
#     os.system(command)
#     time.sleep(1)  # Small delay after executing the command


# # Input event used to insert text into the mobile
# def adbInput(message):
#     """
#     Input text into an Android device via ADB.
#     :param message: The text to input.
#     """
#     command = f'adb shell input text "{message}"'
#     os.system(command)
#     time.sleep(1)  # Small delay after executing the command


# # Go completely back (used in some scenarios where multiple "Back" presses are required)
# def goback(key_code):
#     """
#     Simulate the 'Back' button press multiple times.
#     :param key_code: The keycode for the back button (typically 4).
#     """
#     for i in range(6):  # Press the 'Back' button 6 times
#         keyEvent(key_code)


# # Replace spaces in a string with '%s' (used for sending messages)
# def replace_spaces_with_percent_s(input_string):
#     """
#     Replace spaces in a string with '%s'.
#     Useful for formatting text input in some cases where space needs to be encoded.
#     :param input_string: The input string.
#     :return: The modified string with spaces replaced by '%s'.
#     """
#     return input_string.replace(' ', '%s')
