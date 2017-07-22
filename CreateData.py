import os, time, random


class CreateData:
    def __init__(self, fileDir, fileCount):
        self.fileDir = fileDir
        self.fileCount = fileCount

    def createData(self):
        for i in range(self.fileCount):
            file = open(os.path.join(self.fileDir, "Data-%s.txt" % str(i + 1).zfill(2)), "w", encoding="utf-8",
                        errors="strict")
            for data in range(random.randrange(10), 5000000, 7):
                writeStr = str(data).zfill(7) + "\t" + str(data).zfill(7) + "\n"
                file.write(writeStr)


data = CreateData(r"data", 50)
data.createData()
