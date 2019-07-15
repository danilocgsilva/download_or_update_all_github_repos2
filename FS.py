import os

class FS:

    def get_file_list(self, folder) -> list:
        return os.listdir(folder)
