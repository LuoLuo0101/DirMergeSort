## 文件夹合并算法（处理17亿条数据，120个文件，总共5-80G文件的有序合并只需要6.5小时，单线程）
### 项目CSDN地址：http://blog.csdn.net/heyiaiqing/article/details/75745268

### 项目介绍
#### 第一步：创建数据
1. 首先打开CreateData模块，运行下该模块，你就能在本项目路径下的data下拿到生成的数据，用这个模拟文件夹归并
2. 其次CreateData模块生成了50个文件，总共579M数据，文件夹内文件越多，本项目的优势越能体现出来
3. 运行下Merge模块，然后两分钟五十三秒左右，你就能拿到579M数据组成的一个排好序的大文件，本项目经过了17亿级别的数据测试，没有丢失数据以及其他情况

#### 第二步：Merge合并文件夹数据
1. 首先是打开所有文件，将所有文件都添加到self.fileList列表中
2. 其次循环拿到每一个文件的第一行数据以 [file, [line, line.split("\t")[0]]]的格式添加到一个列表中，形成二维列表
3. file是当前的文件对象，line是你读取到的那行数据，将数据进行分割，然后拿到你要按照第一列进行排序的数据，方便后面进行对比
4. 对数据进行排序，按照第一列的数据进行排序从大到小排序
5. 然后下面的while循环是本项目的精华
6. 首先while循环判断条件是list1不为空，也就是有数据可比
7. 然后因为上面第4条对数据进行了排序，所以拿出第一条数据永远是最小的
8. 将这条数据写入新的大文件中，然后将这条数据从list1中移除
9. 然后再用这个文件读取一行数据，利用二分法查找到需要插入的索引并插入list1列表中
10. 那么list1又是有序的，这个时候你可以你又可以拿到第一行数据，如此循环，那么写入大文件中的数据就是完全有序的

#### 第三步：测试结果(文件越多，二分法插入排序的优势越大)
```
二分法插入归并测试  50个文件 579M  耗时 0:02:53
开始文件夹合并： Sat Jul 22 09:00:14 2017
结束文件夹合并： Sat Jul 22 09:03:07 2017

插入排序归并测试  50个文件 579M  耗时 0:06:47
开始文件夹合并： Sat Jul 22 09:04:19 2017
结束文件夹合并： Sat Jul 22 09:11:06 2017
```