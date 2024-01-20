import os
import shutil

class DirectoryManager:
    def __init__(self, base_directory="."):
        self.base_directory = base_directory

    # def create_directory(self, directory_name):
    #     path = os.path.join(self.base_directory, directory_name)
    #     os.makedirs(path, exist_ok=True)
    #     return f"Directorio {directory_name} creado."

    def list_directories(self):
        directories = [d for d in os.listdir(self.base_directory) if os.path.isdir(os.path.join(self.base_directory, d))]
        return directories

    # def copy_directory(self, source_directory, destination_directory):
    #     source_path = os.path.join(self.base_directory, source_directory)
    #     destination_path = os.path.join(self.base_directory, destination_directory)
    #     shutil.copytree(source_path, destination_path)
    #     return f"Directorio {source_directory} copiado a {destination_directory}."

    # def move_directory(self, source_directory, destination_directory):
    #     source_path = os.path.join(self.base_directory, source_directory)
    #     destination_path = os.path.join(self.base_directory, destination_directory)
    #     shutil.move(source_path, destination_path)
    #     return f"Directorio {source_directory} movido a {destination_directory}."

    # def delete_directory(self, directory_name):
    #     path = os.path.join(self.base_directory, directory_name)
    #     try:
    #         shutil.rmtree(path)
    #         return f"Directorio {directory_name} eliminado."
    #     except FileNotFoundError:
    #         return f"El directorio {directory_name} no existe."

# Ejemplo de uso
directory_manager = DirectoryManager("chatbot")

# Crear directorio
# directory_manager.create_directory("mi_subdirectorio")

# Listar directorios en el directorio principal
directories_in_base_directory = directory_manager.list_directories()
print("Directorios en el directorio principal:", directories_in_base_directory)

# Copiar directorio
# directory_manager.copy_directory("mi_subdirectorio", "copia_mi_subdirectorio")

# Mover directorio
# directory_manager.move_directory("copia_mi_subdirectorio", "mi_subdirectorio_copiado")

# Listar directorios después de mover
# directories_after_move = directory_manager.list_directories()
# print("Directorios después de mover:", directories_after_move)

# Eliminar directorio
# directory_manager.delete_directory("mi_subdirectorio_copiado")
