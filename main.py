#from Test import *
from Body.DeviceManager import *
from Pilot.Pilot import *

#doorTest()
Body = DeviceManager()
Body.createObjects()
print Body.getBodyObjectModel()
print Body.getObjectInstance("door", "FRONT_LEFT")
print Body.getObjectInstance("trunk").isOpened

rc = Pilot("0x0001")
rc.clickOpenDoorButton()
for door in Body.getBodyObjectModel():
    door.isOpened

rc.clickCloseDoorButton()
for door in Body.getBodyObjectModel():
    door.isOpened

rc.clickSwitchTrunkButton()
print Body.getObjectInstance("trunk").isOpened

rc.clickSwitchTrunkButton()
print Body.getObjectInstance("trunk").isOpened