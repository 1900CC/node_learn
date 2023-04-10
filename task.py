# import time
# scale = 50
# print("Please Wait".center(scale+8,"="))
# for i in range(scale+1):
#     a = "█" * i
#     b = "." * (scale - i)
#     c =( i/scale)*100
#     print("\r{:^3.0f}%[{}>{}]".format(c,a,b),end='')
#     time.sleep(0.05)
# print("\n","finish".center(scale+8,"="))

# from xlwt import Workbook

# #创建一个工作簿
# w = Workbook()
# #创建一个工作表
# ws = w.add_sheet('1')
# # 计数
# count = 0
# # 行数
# link_nums = 5000
# for j in range(0,2):     #控制列
#     for i in range(0, link_nums):   #控制行
#         count += 1

#         if(j == 0):         #第一列
#             ws.write(i, j, i)
#         if(j == 1):
#             ws.write(i,j,i)
# print("总共生成(单元格): %s数据"%count)
# print("总共生成: %s条数据"%link_nums)

# w.save('xqtest.xls')

import datetime
import time

times = datetime.datetime.now().strftime('%Y-%m-%d')
# print(times)

# # 获取当前时间
# times=datetime.datetime.now().strftime('%Y-%m-%d')
# print(times)
# # 转为时间数组
# timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
# # 转为时间戳
# timeStamp = int(time.mktime(times))
# print(timeStamp)
# print(int(time.mktime(time.localtime(time.time()))))
# times = datetime.datetime.now().strftime('%Y-%m-%d')
# ctime = datetime.datetime.strptime(times, '%Y-%m-%d').timestamp()
# print(ctime)

# t = time.time()  # 当前时间

# print(t)  # 原始时间数据
# print(int(t))  # 秒级时间戳
# print(int(round(t * 1000)))  # 毫秒级时间戳
# print(int(round(t * 1000000)))  # 微秒级时间戳

# # 获得当前时间时间戳
# now = int(time.time())
# print(now)
# #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
# timeArray = time.localtime(now)
# otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
# print(otherStyleTime)


# times = datetime.datetime.now().strftime('%Y-%m-%d')
# # print(times)
# # def show_day(string):
# #     return time.strptime(string,"%Y-%m-%d")
# # print(show_day("2019-9-1").tm_yday)      


# print(time.strptime(datetime.datetime.now().strftime('%Y-%m-%d'),"%Y-%m-%d").tm_yday - time.strptime("04-06","%m-%d").tm_yday)

