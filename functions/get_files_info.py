import os

def get_files_info(working_directory, directory="."):
    folderpath = os.path.join(working_directory, directory)
    try:
        if directory == ".":
            print(f"Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")
        if not os.path.isdir(folderpath):
            return f"Error: '{directory}' is not a directory\n"
        if not os.path.abspath(working_directory) in os.path.abspath(folderpath):
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory\n"
        file_list = ""
        for file in os.listdir(folderpath):
            filepath = os.path.join(folderpath, file)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            file_list += f" - {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
        return file_list
    except:
        raise Exception("Error: didn't work") 