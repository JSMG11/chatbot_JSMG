import os
import shutil


class Directory:
    def __init__(self, path):
        self.path = path

    def list_files(self):
        """
        List files in the directory.

        Returns:
            list: List of filenames in the directory.
        """
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        return files

    def create_file(self, name):
        """
        Create a new file in the directory.

        Args:
            name (str): Name of the file to be created.
        """
        file_path = os.path.join(self.path, name)
        with open(file_path, 'w') as file:
            file.write('')

    def create_directory(self, name):
        """
        Create a new directory in the current directory.

        Args:
            name (str): Name of the directory to be created.
        """
        directory_path = os.path.join(self.path, name)
        os.makedirs(directory_path)

    def rename_directory(self, new_name):
        """
        Rename the current directory.

        Args:
            new_name (str): New name for the directory.
        """
        new_path = os.path.join(os.path.dirname(self.path), new_name)
        os.rename(self.path, new_path)
        self.path = new_path

    def search_file(self, name):
        """
        Search for files that contain the specified name.

        Args:
            name (str): Name or part of the name to search for.

        Returns:
            list: List of filenames that match the search criteria.
        """
        matches = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f)) and name.lower() in f.lower()]
        return matches

    def move_file(self, file_path, destination_path):
        """
        Move a file to a new destination.

        Args:
            file_path (str): Path of the file to be moved.
            destination_path (str): Destination path for the file.
        """
        shutil.move(file_path, os.path.join(destination_path, os.path.basename(file_path)))
