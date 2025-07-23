import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    absfile = os.path.join(working_directory, file_path)
    try:
        if not os.path.abspath(working_directory) in os.path.abspath(absfile):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absfile):
            return f'Error: File "{file_path}" not found.'
        if not absfile.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        # completed_process = subprocess.run(absfile,)
        # return completed_process
        #return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        raise Exception("Error: didn't work") 