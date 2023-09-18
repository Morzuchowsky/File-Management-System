import os


# Create a new directory.
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully!")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory '{directory_name}': {e}")


# List all files in the current directory.
def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    return files


# Delete selected files from the directory.
def delete_files(files_to_delete):
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"'{file}' has been deleted successfully!")
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")


# Rename a file.
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}' successfully!")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except Exception as e:
        print(f"Error renaming file: {e}")


# Move files to a new directory.
def move_files(files_to_move, directory_name):
    if not os.path.exists(directory_name):
        print(f"Directory '{directory_name}' does not exist. Creating it now.")
        create_directory(directory_name)

    for file in files_to_move:
        try:
            os.replace(file, os.path.join(directory_name, file))
            print(f"'{file}' moved to '{directory_name}' successfully!")
        except Exception as e:
            print(f"Error moving '{file}': {e}")


# Main function to execute the script.
def main():
    # Example usage
    create_directory("new_directory")
    files = list_files()
    print(f"Files in current directory: {files}")
    delete_files(["sample.txt"])
    rename_file("old_name.txt", "new_name.txt")
    move_files(["file1.txt", "file2.txt"], "new_directory")


if __name__ == "__main__":
    main()
