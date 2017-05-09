# 排序问题
# tmp_list = []
#
# def func(x, y):
#     len_1 = len(x)
#     len_2 = len(y)
#     if len_1 == 0:
#         tmp_list.extend(y)
#         return
#     if len_2 == 0:
#         tmp_list.extend(x)
#     if x[0] <= y[0]:
#         tmp_list.append(x[0])
#         func(x[1:], y)######切片将数组第一位切去
#     else:
#         tmp_list.append(y[0])
#         func(x, y[1:])
#     return tmp_list
# a = [1, 3, 5, 7, 9]
# b = [2, 4, 6, 8, 10]
# print(func(a,b))
#
#
# # # 水桶问题
# count = []
# def find41(a=0):
#     if len(count) > 1000:
#         assert False
#     if a in count:
#         assert False
#     if a in [10, 21]:
#         count.append(a)
#         return
#     if a + 31 > 51:
#         count.append(a)
#         find41(a+31-51)
#     if a + 31 < 51:
#         count.append(a)
#         find41(a + 62 -51)
#
#     return count
# print(find41(a=0))

####提取数据
l1=['hello',12,'hh','dee',None]
L2=[s.lower() for s in l1 if isinstance(s,str)]#####从l1中提取字符串数据
print(L2)

def bubble_sort(list):######冒泡排序
    count=len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if list[i] > list[j]:
                list[i],list[j]=list[j],list[i]
    return list