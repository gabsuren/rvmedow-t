from models.credentials import Credentials
from models.file_system import FileSystem


class Workload(FileSystem):
    """Workload class

    Attributes:
        ip (str): IP address
        cred (Credentials):
        storage (list): list of instances of type MountPoint
    """

    def __init__(self, ip, cred, storage):
        assert isinstance(ip, str)
        assert isinstance(cred, Credentials)
        assert isinstance(storage, list)

        self.ip = ip
        self.cred = cred
        self.storage = storage
