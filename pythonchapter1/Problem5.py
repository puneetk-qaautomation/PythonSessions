import os  # Import the os module

# Label the program written in problem 4 with coments:
# Function to list contents of a directory
def list_directory_contents(path='/'):
    try:
        # Get list of files and folders in the given path
        items = os.listdir(path)

        print("Contents of directory:", os.path.abspath(path))
        print("-------------------------------")

        # Loop through each item in the list
        for item in items:
            full_path = os.path.join(path, item)  # Get full path of the item

            # Check if the item is a directory
            if os.path.isdir(full_path):
                print("[DIR] ", item)
            else:
                print("      ", item)

    except FileNotFoundError:
        print("The directory was not found.")
    except PermissionError:
        print("You do not have permission to access this directory.")


# Call the function for current directory
list_directory_contents()
