import os

#renombre, eliminacion y cambio de permisos de archivo
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
        try:
            os.chmod(self.path, permissions)
            print(f"Permisos cambiados correctamente para {self.path}")
        except OSError as e:
            print(f"Error al cambiar permisos para {self.path}: {e}")
