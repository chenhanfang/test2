import csv
filename='xxx.csv'
with open(filename) as f:
    reader = csv.reader(f)#####读取文件内容
    header_row = next(reader)
    print(header_row)

    for index,column_header in enumerate(header_row):#######enmuerate来获取每个元素的索引及其值
        print(index,column_header)
        ######population=int(float(pop-dict['value']))float将字符串转为小数，int会丢弃小数部分
