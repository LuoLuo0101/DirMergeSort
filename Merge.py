import time, os

'''
create by Luo 2017-7-22 14:53:21
'''
class Merge:
    def __init__(self, orginDir, objectPath):
        self.fileNameList = os.listdir(orginDir)  # 文件夹下所有文件名
        self.fileList = []  # 文件列表
        self.objectFile = open(objectPath, "w", -1, encoding="utf-8", errors="strict")  # 目标文件
        for fileName in self.fileNameList:  # 遍历添加文件到文件列表
            file = open(os.path.join(orginDir, fileName), "r", -1, encoding="utf-8", errors="strict")
            self.fileList.append(file)

    # 文件夹合并
    def mergeFile(self):
        print("开始文件夹合并：", time.ctime())
        list1 = []  # 用于装文件对象，文件读取的数据，以及排序的那一列数据
        # 循环拿到每一个文件的第一行数据并添加进列表
        for file in self.fileList:
            line = file.readline()
            if line:
                list1.append([file, [line, line.split("\t")[0]]])
            else:
                file.close()  # 剔除无用的文件
                self.fileList.remove(file)

        list1.sort(key=lambda x: x[1][1])  # 只进行一次排序

        while len(list1) != 0:
            # 将排序最小的数据写入文件，并剔除文件末尾的错位情况
            self.objectFile.write(list1[0][1][0])
            nowFile = list1[0][0]
            nowLine = nowFile.readline()
            list1.remove(list1[0])
            if nowLine:  # 过滤读到文件末尾的情况，并把该文件剔除
                # self.__insertAndSort(list1, [nowFile, [nowLine, nowLine.split("\t")[0]]])  # 插入排序，节省排序时间
                self.__helfInsert(list1, [nowFile, [nowLine, nowLine.split("\t")[0]]])  # 插入排序，节省排序时间
            else:
                nowFile.close()
        print("结束文件夹合并：", time.ctime())

    # 插入排序，节省排序时间
    def __insertAndSort(self, list1, listItem):
        for index in range(len(list1)):
            if listItem[1][1] <= list1[index][1][1]:
                list1.insert(index, listItem)
                break
        else:
            list1.append(listItem)

    # 二分法插入排序
    def __helfInsert(self, list1, listItem):
        num1 = listItem[1][1]
        low = 0
        length = len(list1)
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            if num1 < list1[mid][1][1]:
                high = mid - 1
            elif num1 > list1[mid][1][1]:
                low = mid + 1
            else:
                list1.insert(mid, listItem)
                break
        else:
            if low == length:
                list1.append(listItem)
            else:
                list1.insert(low, listItem)

    def __del__(self):
        self.objectFile.close()


orginDir = r"data"
objectPath = r"DirMergeSort.txt"

merge1 = Merge(orginDir, objectPath)
merge1.mergeFile()

# 二分法插入归并测试  50个文件 579M  耗时 0:02:53
# 开始文件夹合并： Sat Jul 22 09:00:14 2017
# 结束文件夹合并： Sat Jul 22 09:03:07 2017

# 插入排序归并测试  50个文件 579M  耗时 0:06:47
# 开始文件夹合并： Sat Jul 22 09:04:19 2017
# 结束文件夹合并： Sat Jul 22 09:11:06 2017