import os
from enum import Enum, auto

class Unit(Enum):
    KB = auto()
    MB = auto()
    GB = auto()

def getDirSize(targetPath : str) -> int:
    if targetPath is None:
        return 0

    fileList = os.listdir(targetPath)   
    
    size = 0

    for fileName in fileList:
        fullPath = f"{targetPath}/{fileName}"
        if os.path.isdir(fullPath) :
            size += getDirSize(fullPath)
        elif os.path.isfile(fullPath):
            size += os.path.getsize(fullPath)
    
    return size


def getByte(size : int, count : int) -> float:
    for i in range(0, count):
        size = size / 1024
    return round(size, 4)