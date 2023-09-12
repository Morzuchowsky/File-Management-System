import os
import shutil
import re


def delete_files(extension, start_dir):
    """Delete files with a given extension from a directory and its subdirectories."""
    print(f"\nAre you sure that you want to delete all files with the file type: {extension.upper()}")
    print(f"from: {start_dir} and all sub-folders")

    confirmation = input("Y or N? ").upper()
    while confirmation not in ["Y", "N"]:
        confirmation = input("Y or N? ").upper()

    if confirmation == 'Y':
        for current_folder, _, filenames in os.walk(start_dir, topdown=False):
            for filename in filenames:
                if extension == "*" or filename.endswith('.' + extension):
                    os.remove(os.path.join(current_folder, filename))
            if current_folder != start_dir:
                try:
                    os.rmdir(current_folder)
                except:
                    pass

        print("\nFile and Sub-Folder Deletion Completed")
    else:
        print("\nFile and Sub-Folder Deletion Canceled")


def copy_files(extension, start_dir, end_dir):
    """Copy files with a given extension from a directory and its subdirectories to another directory."""
    print(f"\nAre you sure that you want to copy all files with the file type: {extension.upper()}")
    print(f"from: {start_dir} and all sub-folders to: {end_dir}")

    confirmation = input("Y or N? ").upper()
    while confirmation not in ["Y", "N"]:
        confirmation = input("Y or N? ").upper()

    if confirmation == 'Y':
        for current_folder, _, filenames in os.walk(start_dir, topdown=False):
            regex = re.compile(re.escape(start_dir) + r"(\\.*)")
            subcurrent_folder = re.findall(regex, current_folder)
            current_end_dir = end_dir + subcurrent_folder[0] if subcurrent_folder else end_dir

            os.makedirs(current_end_dir, exist_ok=True)

            for filename in filenames:
                if extension == "*" or filename.endswith('.' + extension):
                    shutil.copy(os.path.join(current_folder, filename), os.path.join(current_end_dir, filename))

        print("\nFile and Sub-Folder Copying Completed")
    else:
        print("\nFile and Sub-Folder Copying Canceled")


def move_files(extension, start_dir, end_dir):
    """Move files with a given extension from a directory and its subdirectories to another directory."""
    print(f"\nAre you sure that you want to move all files with the file type: {extension.upper()}")
    print(f"from: {start_dir} and all sub-folders to: {end_dir}")

    confirmation = input("Y or N? ").upper()
    while confirmation not in ["Y", "N"]:
        confirmation = input("Y or N? ").upper()

    if confirmation == 'Y':
        for current_folder, _, filenames in os.walk(start_dir, topdown=False):
            regex = re.compile(re.escape(start_dir) + r"(\\.*)")
            subcurrent_folder = re.findall(regex, current_folder)
            current_end_dir = end_dir + subcurrent_folder[0] if subcurrent_folder else end_dir

            os.makedirs(current_end_dir, exist_ok=True)

            for filename in filenames:
                if extension == "*" or filename.endswith('.' + extension):
                    shutil.move(os.path.join(current_folder, filename), os.path.join(current_end_dir, filename))
            if current_folder != start_dir:
                try:
                    os.rmdir(current_folder)
                except:
                    pass

        print("\nFile and Sub-Folder Moving Completed")
    else:
        print("\nFile and Sub-Folder Moving Canceled")


def main():
    action = input("Choose action (Copy, Move or Delete): ").capitalize()
    extension = input("File Type (\"*\" for all files): ")

    start_dir = input(f"Directory to {action} from: ")
    while not os.path.exists(start_dir):
        print("Please check that the directory exists.")
        start_dir = input(f"Directory to {action} from: ")

    end_dir = ""
    if action in ['Copy', 'Move']:
        end_dir = input(f"Directory to {action} to: ")

    if action == 'Delete':
        delete_files(extension, start_dir)
    elif action == 'Copy':
        copy_files(extension, start_dir, end_dir)
    elif action == 'Move':
        move_files(extension, start_dir, end_dir)
    else:
        print("\nError determining action")


if __name__ == "__main__":
    main()
