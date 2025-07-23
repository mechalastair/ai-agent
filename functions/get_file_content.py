import os
from config import character_limit

def get_file_content(working_directory, file_path):
    absfile = os.path.join(working_directory, file_path)
    try:
        if not os.path.abspath(working_directory) in os.path.abspath(absfile):
            return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory\n"
        if not os.path.isfile(absfile):
            return f"Error: File not found or is not a regular file: '{file_path}'"
        text_len = os.path.getsize(absfile)
        text = str(os.read(os.open(absfile, os.O_RDONLY), character_limit))
        if text_len > character_limit:
            text += f"[...File '{file_path}' truncated at {character_limit} characters]"
        return text
    except:
        raise Exception("Error: didn't work") 