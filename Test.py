from Body.Door import *

def doorTest():
    door = Door("door", "FRONT_LEFT")
    if door.isOpened == False:
        print "[TEST]: First condition passed"
    else:
        print "[TEST]: First condition failed"
    door.openDoor()
    if door.isOpened == True:
        print "[TEST]: Second condition passed"
    else:
        print "[TEST]: First condition failed"
    door.closeDoor()
    if door.isOpened == False:
        print "[TEST]: First condition passed"
    else:
        print "[TEST]: First condition failed"


