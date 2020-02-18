from models.credentials import Credentials
from models.workload import Workload
from models.file_system import FileSystem
from enum import Enum


class CloudType(Enum):
    AWS = 1
    AZURE = 2
    VSPHERE = 3
    VCLOUD = 4


class MigrationTarget(FileSystem):
    """MigrationTarget class

    Attributes:
        type (CloudType): Cloud type.
        credentials (Credentials): Cloud Credentials.
        vm (Workload): Target Virtual Machine.
    """

    def __init__(self, type, credentials, vm):
        assert isinstance(type, CloudType)
        assert isinstance(vm, Workload)
        assert isinstance(credentials, Credentials)

        self.type = type
        self.credentials = credentials
        self.vm = vm


