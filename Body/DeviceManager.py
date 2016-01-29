
from Body.Mask import *
from Body.Trunk import *

class DeviceManager:

    _BODY_OBJECTS = []

    def __init__(self):
        self.EMU = open(GLOBALS["EMU"], "r")
        self.content = self.EMU.readlines()
        print __name__ + str(self.content)

    def createObjects(self):
        detectedObjs = self.content[0].split(":")
        for element in detectedObjs:
            if element.find("door") != -1:
                numberOfElement = int(element.split("[")[1][:-1])
                self._createDoor(numberOfElement)
            elif element.find("mask") != -1:
                self._BODY_OBJECTS.append(Mask())
            elif element.find("trunk") != -1:
                self._BODY_OBJECTS.append(Trunk())

    def _createDoor(self, number):
        for i in range(number):
            if i == 0:
                 self._BODY_OBJECTS.append(Door("door", "FRONT_LEFT"))
            elif i == 1:
                 self._BODY_OBJECTS.append(Door("door", "FRONT_RIGHT"))
            elif i == 2:
                 self._BODY_OBJECTS.append(Door("door", "BACK_LEFT"))
            elif i == 3:
                 self._BODY_OBJECTS.append(Door("door", "BACK_RIGHT"))

    def getBodyObjectModel(self):
        return self._BODY_OBJECTS

    def getObjectInstance(self, type, pos=None):
        for object in self._BODY_OBJECTS:
            if object.type == type and type != "door":
                return object
            elif object.type == type and type == "door":
                if object.pos == pos:
                    return object
                else:
                    pass

    def openEachDoor(self):
        for door in self.getBodyObjectModel():
            door.openDoor()

    def closeEachDoor(self):
        for door in self.getBodyObjectModel():
            door.closeDoor()