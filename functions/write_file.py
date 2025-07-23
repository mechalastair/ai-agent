import os

def write_file(working_directory, file_path, content):
    absfile = os.path.join(working_directory, file_path)
    try:
        if not os.path.abspath(working_directory) in os.path.abspath(absfile):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        os.makedirs(os.path.dirname(absfile), exist_ok=True)
        with open(absfile, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        raise Exception("Error: didn't work") 