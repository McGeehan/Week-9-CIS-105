import pyperclip
import webbrowser
import time

# This function will open Google Maps with directions to the provided address
def open_google_maps(address):
    base_url = "https://www.google.com/maps/dir/?api=1&destination="
    destination = address.replace(" ", "+")  # Replace spaces with '+' for URL encoding
    url = base_url + destination
    webbrowser.open(url, new=2)

# Continuously monitor the clipboard for changes
previous_clipboard_content = None
while True:
    # Get the current clipboard content
    clipboard_content = pyperclip.paste()

    # If the clipboard content has changed, open Google Maps with the new address
    if clipboard_content != previous_clipboard_content:
        print("New address copied:", clipboard_content)
        open_google_maps(clipboard_content)
        previous_clipboard_content = clipboard_content

    # Pause for a short time before checking the clipboard again
    time.sleep(1)
