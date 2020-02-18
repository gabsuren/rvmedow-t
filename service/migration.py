import time

from models.workload import Workload
from models.migration_target import MigrationTarget
from enum import Enum


class State(Enum):
    NOT_START = 1
    RUNNING = 2
    ERROR = 3
    SUCCESS = 4


class Migration:
    """Migration class

    Attributes:
        sel_mps (list): Selected Mount points
        source (Workload): Source
        target (MigrationTarget): Migration Target
    """

    def __init__(self, sel_mps, source, target):
        assert isinstance(sel_mps, list)
        assert isinstance(source, Workload)
        assert isinstance(target, MigrationTarget)

        self.source = source
        self.sel_mps = sel_mps
        self.target = target
        self.state = State.NOT_START

    def run(self):
        if not any(x.name == "C:" for x in self.sel_mps):
            raise Exception("C: is not selected")

        # desired = set(self.source.storage).intersection(self.mount_points)
        for s in self.sel_mps:  # Selected mount points
            for x in self.source.storage:  # Source mount points
                if s.name == x.name:
                    self.state = State.RUNNING
                    result = self.copy(self.source.storage, self.target.vm.storage)
                    if result:
                        self.state = State.SUCCESS
                    else:
                        self.state = State.ERROR

    # This is dummy method for now, should copy source mount point to the target
    # Copy source object to the Migration Target.Target VM  and
    def copy(self, source, target):
        time.sleep(10)
        return True
