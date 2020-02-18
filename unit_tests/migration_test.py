import unittest
from models.migration_target import MigrationTarget, CloudType
from models.mount_point import MountPoint
from models.credentials import Credentials
from models.workload import Workload
from service.migration import Migration


class MigrationTest(unittest.TestCase):
    """
        This class provides simple checks for Migration class
    """

    def test_wrong_type_throws_exception(self):
        self.assertRaises(AssertionError, MigrationTarget('Wrong type', 'Wrong type', 'Wrong type'))

    def test_C_dir_not_selected(self):
        mp1 = MountPoint("D:", 10)
        mps = [mp1]
        cr1 = Credentials('usr', 'psw', 'aws.com')
        source = Workload('10.1.1.1', cr1, mps)

        # Migration Target
        mp1_t = MountPoint("E:", 10)
        mps_t = [mp1_t]
        cr2 = Credentials('usr', 'psw', 'azure.com')
        target = MigrationTarget(CloudType.AZURE, cr2, Workload('10.0.0.0', cr2, mps_t))

        # Start migration
        sel_mnt_pnt = [mp1]
        migration = Migration(sel_mnt_pnt, source, target)
        self.assertRaises(Exception, migration.run())

    if __name__ == '__main__':
        unittest.main()