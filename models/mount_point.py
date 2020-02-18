from models.file_system import FileSystem


class MountPoint(FileSystem):
    """MountPoint class

    Attributes:
        name (str): Mount point name
        size (int): Total size of the volume
    """

    def __init__(self, name, size):
        assert isinstance(name, str)
        assert isinstance(size, int)

        self.name = name
        self.size = size
