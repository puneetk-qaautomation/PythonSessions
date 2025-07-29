import os


def list_directory_contents(path='/Users'):
    try:
        # Get the list of all files and directories
        contents = os.listdir(path)

        print(f"Contents of directory: {os.path.abspath(path)}\n")
        for item in contents:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"       {item}")
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")


# Example usage: current directory
list_directory_contents()
