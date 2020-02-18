from models.migration_target import MigrationTarget, CloudType
from models.mount_point import MountPoint
from models.credentials import Credentials
from models.workload import Workload
from service.migration import Migration


mp1 = MountPoint("D:", 10)
mp2 = MountPoint("C:", 20)
mp3 = MountPoint("E:", 30)
mps = [mp1, mp2, mp3]

# Migration Source
cr1 = Credentials('usr', 'psw', 'aws.com')
source = Workload('10.1.1.1', cr1, mps)
cr1.save()
source.save()

# Migration Target
mp1_t = MountPoint("E:", 10)
mp2_t = MountPoint("C:", 20)
mps_t = [mp1_t, mp2_t]
cr2 = Credentials('usr', 'psw', 'azure.com')
target = MigrationTarget(CloudType.AZURE, cr2, Workload('10.0.0.0', cr2, mps_t))
cr2.save()
target.save()

# Start migration
sel_mnt_pnt = [mp2]
migration = Migration(sel_mnt_pnt, source, target)
migration.run()
