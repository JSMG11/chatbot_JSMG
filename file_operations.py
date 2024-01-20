import os
import textwrap
class FileManager:
    def __init__(self, directory="."):
        self.directory = directory

    def list_files(self):
        files = os.listdir(self.directory)
        return files



if __name__ == "__main__":
    print("                __________")
    print("         ______/ ________ \______")
    print("       _/      ____________      \_")
    print("     _/____________    ____________\_")
    print("   */  ___________ \  / ___________  \*")
    print("  */  /XXXXXXXXXXX\ \/ /XXXXXXXXXXX\  \*")
    print(" */  /############/    \############\  \*")
    print("  |  \XXXXXXXXXXX/ _  _ \XXXXXXXXXXX/  |")
    print("__|\_____   ___   //  \\   ___   _____/|__")
    print("[_       \     \  X    X  /     /       _]")
    print("__|     \ \                    / /     |__")
    print("[____  \ \ \   ____________   / / /  ____]")
    print("     \  \ \ \/||.||.||.||.||\/ / /  /")
    print("      \_ \ \  ||.||.||.||.||  / / _/")
    print("        \ \   ||.||.||.||.||   / /")
    print("         \_   ||_||_||_||_||   _/")
    print("           \     ........     /")
    print("            \________________/")

    print("\nHola soy databot en que puedo ayudarte el dia de hoy?:\n")

    file_manager = FileManager()
    files_in_directory = file_manager.list_files()
    print("Archivos en el directorio:", files_in_directory)
