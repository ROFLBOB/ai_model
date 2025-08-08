import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'