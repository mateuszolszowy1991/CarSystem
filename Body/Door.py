from . import *
class Door:

    type=''
    pos=''
    isOpened = False

    def __init__(self, type, pos):
        if self.__verifyArgs(type, pos):
            self.type = type
            self.pos = pos
            print __name__ + "[INFO]: Door created"

    def __verifyArgs(self, type, pos):
        if type in TYPES and pos in POSITIONS:
            return True

    def openDoor(self):
        if self.isOpened:
            print __name__ + " [WARNING] + One or more doors is opened. "
        else:
            self.isOpened = True
            print __name__ + " [INFO]:" + self.type + " " + self.pos + " is opened"

    def closeDoor(self):
        if self.isOpened:
            self.isOpened = False
            print __name__ + " [INFO]:" + self.type + " " + self.pos + " is closed "
        else:
            print __name__ + " [WARNING] + Doors is already closed"
