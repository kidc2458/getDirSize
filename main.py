import getDirSize

if __name__ == "__main__":
    path = "D:/Nexon"
    size = getDirSize.getDirSize(path)

    print(getDirSize.getByte(size,getDirSize.Unit.GB.value))