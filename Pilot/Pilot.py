from Pilot import *
from Body.DeviceManager import *
class Pilot:
    
    def __init__(self, id):
        self.loadData(id)
        if self.checkIsRegistered(id):
            self.subscribeToDoor()
            print __name__ + "[INFO]: Pilot is reistered for: " + self.content.split(":")[1]

    def subscribeToDoor(self):
        self.doorDevMan = DeviceManager()


    def checkIsRegistered(self, id):
        if len(self.content.split(":")) > 0:
            return True

    def loadData(self, id):
        f = open("Pilot/userID.txt", "r")
        content = f.readlines()
        f.close()
        for user in content:
            if id in user:
                self.content = user


    def getUserInfo(self):
        self.content

    def clickOpenDoorButton(self):
        self.doorDevMan.openEachDoor()

    def clickCloseDoorButton(self):
        self.doorDevMan.closeEachDoor()

    def clickSwitchTrunkButton(self):
        trunk = self.doorDevMan.getObjectInstance("trunk")
        if trunk.isOpened:
            trunk.isOpened = False
        else:
            trunk.isOpened = True
