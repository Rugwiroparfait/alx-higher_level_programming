#!/usr/bin/python3

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, "w", encoding="UTF-8") as f:
        num_characters_written = f.write(text)
    return num_characters_written

