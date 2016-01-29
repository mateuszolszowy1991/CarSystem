from Body.Door import *

class Mask(Door):

    def __init__(self):
        self.type = "mask"
        self.isOpened = False
        print __name__ + "[INFO]: Mask created"

