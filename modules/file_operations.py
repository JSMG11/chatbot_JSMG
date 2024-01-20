
# if __name__ == "__main__":
#     print("                __________")
#     print("         ______/ ________ \______")
#     print("       _/      ____________      \_")
#     print("     _/____________    ____________\_")
#     print("   */  ___________ \  / ___________  \*")
#     print("  */  /XXXXXXXXXXX\ \/ /XXXXXXXXXXX\  \*")
#     print(" */  /############/    \############\  \*")
#     print("  |  \XXXXXXXXXXX/ _  _ \XXXXXXXXXXX/  |")
#     print("__|\_____   ___   //  \\   ___   _____/|__")
#     print("[_       \     \  X    X  /     /       _]")
#     print("__|     \ \                    / /     |__")
#     print("[____  \ \ \   ____________   / / /  ____]")
#     print("     \  \ \ \/||.||.||.||.||\/ / /  /")
#     print("      \_ \ \  ||.||.||.||.||  / / _/")
#     print("        \ \   ||.||.||.||.||   / /")
#     print("         \_   ||_||_||_||_||   _/")
#     print("           \     ........     /")
#     print("            \________________/")

import os


class File:
    def __init__(self, path):
        self.path = path

    def rename(self, new_name):
        """
        Rename the file.

        Args:
            new_name (str): New name for the file.
        """
        new_path = os.path.join(os.path.dirname(self.path), new_name)
        os.rename(self.path, new_path)
        self.path = new_path

    def delete(self):
        """
        Delete the file.
        """
        os.remove(self.path)

    def change_permissions(self, permissions):
        """
        Change the file permissions.

        Args:
            permissions (int): New permissions to set for the file.
        """
        os.chmod(self.path, permissions)
