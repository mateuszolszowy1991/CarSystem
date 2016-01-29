from Body.Door import *

class Trunk(Door):

    def __init__(self):
        self.type = "trunk"
        self.isOpened = False
        print __name__ + "[INFO] Trunk created"



