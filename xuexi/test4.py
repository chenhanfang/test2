# from difflib import SequenceMatcher
# import difflib
# from difflib_data import *
#
# s1={1,2,3,5,6,4}
# s2={2,3,5,4,6,1}
# print('Initial data')
# print('s1=',s1)
# print('s2=',s2)
# print('s1==s2:',s1==s2)
#
# matcher = difflib.SequenceMatcher(None,s1,s2)
# for tag,i1,i2,j1,j2 in reversed(matcher.get_opcodes()):
#     if tag == 'delete':
#         print('Remove %s from positions [%d:%d]'%(s1[i1:i2],i1,i2))
#         del s1[i1:i2]
#     elif tag == 'equal':
#         print('s1[%d:%d] and s2[%d:%d] are the same'%(i1,i2,j1,j2))
#
#     elif tag == 'insert':
#         print('Insert %s from s2[%d:%d] into s1 at %d'%(s2[j1:j2],j1,j2,i1))
#         s1[i1:i2] = s2[j1:j2]
#
#     elif tag == 'replace':
#         print('Replace %s from s1[%d:%d]with %s from s2[%d:%d]'%(s1[i1:i2],i1,i2,s2[j1:j2],j1,j2))
#         s1[i1:i2] = s2[j1:j2]
#
#     print('s1=',s1)
# print('s1 == s2:',s1==s2)


import collections####容器数据类型
# print(collections.Counter(['a','b','c','a','b','b']))
# print(collections.Counter({'a':2,'b':3,'c':1}))
# print(collections.Counter(a=2,b=3,c=1))

# c=collections.Counter()####创建一个空的，然后通过update增加
# print('Initial:',c)
# c.update('abcdaab')
# print('Sequence:',c)
# c.update({'a':1,'d':5})
# print('Dict  :',c )

# d = collections.Counter('abcdaab')
# for letter in 'abcde':####对于未知的元素，输入中未找到该元素计数为0
#     print('%s:%d'%(letter,d[letter]))

# e = collections.Counter('extremely')
# e['z'] = 0
# print(e)
# print(list(e.elements()))####elements()方法返回一个迭代器，将生成Counter的所有元素，小于等于0的元素不包含在内
#
# print('most common:')
# for letter,count in e.most_common(2):######most_common可以生成一个序列，其中包含n个最常遇到的输入值及其相应的计数
#     print('%s:%7d'%(letter,count))

# c1 = collections.Counter(['a','b','c','a','b','b'])####Counter实例支持算数和集合 操作来完成结果的聚集
# c2 = collections.Counter('alphabet')
# print('C1:',c1)
# print('C2:',c2)
# print('\nCombined counts:')
# print(c1+c2)
# print('\nSubtraction:')
# print(c1-c2)
# print('\nIntersection (taking positive mininums):')
# print(c1&c2)
# print('\nUnion (taking maximuns):')
# print(c1 | c2)

# def default_factory():###标准字典包括一个方法setdefault()获取一个值，如果这个值不存在就建立个默认值
#     return 'default value'
# d = collections.defaultdict(default_factory,foo='bar')
# print('d:',d)
# print('foo =>',d['foo'])
# print('bar =>',d['bar'])

# f = collections.deque('abcdefg')####deque(双端队列）支持从任意一端增加或删除元素
# print('Deque:',f)
# print('Length:',len(f))
# print('Left end:',f[0])
# print('Right end:',f[-1])
# f.remove('c')
# print('remove(c):',f)

# d1 = collections.deque()####deque可以从任意一端填充
# d1.extend('abcdefg')
# print('extend   :',d1)
# d1.append('h')
# print('append  :',d1)
# d2 = collections.deque()
# d2.extendleft(range(6))
# print('extendleft :',d2)
# d2.appendleft(6)
# print('appendleft:',d2)


# print('From the right:')
# d3 = collections.deque('abcdefg')
# while True:
#     try:
#         print(d3.pop())####pop()从deque的右端删除元素
#     except IndexError:
#         break
#
# print('\nFrom the left:')
# d3 = collections.deque(range(6))
# while True:
#     try:
#         print(d3.popleft())#####popleft()从deque的左端删除元素
#     except IndexError:
#         break


# import threading,time
# candle = collections.deque(range(5))
# def burn(dirrection,nextSource):
#     while True:
#         try:
#             next = nextSource()
#         except IndexError:
#             break
#         else:
#             print('%s: %s'%(dirrection,next))
#             time.sleep(0.1)
#     print('%8s done'%dirrection)
#     return
# left = threading.Thread(target=burn,args=('Left',candle.popleft))####不同的线程中同时从两端利用队列
# right = threading.Thread(target=burn,args=('Right',candle.pop))#####交替处理两端，删除元素，直至为空
# left.start()
# right.start()
#
# left.join()
# left.join()

# d4 = collections.deque(range(10))
# print('Normal   :',d4)
# d4.rotate(2)######任意一个方向旋转，而跳过一些元素
# print('Right rotation:',d4)
# d4.rotate(-3)
# print('Left rotation :',d4)

# bob = ('Bob',30,'male')
# print('Representation :',bob)
# jane = ('Jane',29,'female')
# print('\nField by index:',jane[0])######使用数值索引访问其成员
# print('\nFields by index:')
# for p in [bob,jane]:
#     print('%s is a %d year  old %s'%p)
#
# Person = collections.namedtuple('Person','name age gender')####使用namedtuple()工厂函数来创建，参数就是新类名和一个包含元素名的字符串
# print('Type of Person:',type(Person))
# bob = Person(name='Bob',age=30,gender='male')
# print('\nRepresentation:',bob)
# jane = Person(name='Jane',age=29,gender='female')
# print('\nFields by name:',jane.name)
# print('\nFields by index:')
# for p in [bob,jane]:
#     print('%s is a %d year old %s'%p)


# with_class = collections.namedtuple('Person','name class age gender',rename=True)
# print(with_class._fields)
# two_ages = collections.namedtuple('Person','name age gender age',rename=True)###重命名的字段的心目，名字取决于再tuple中的索引
# print(two_ages._fields)

# print('Regular dictionary:')
# d = {}
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# for k,v in d.items():
#     print(k,v)
# print('\nOrderdDict:')
# d = collections.OrderedDict()####OrderedDict是一个字典子类，可以记住其内容增加的顺序
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# for k,v in d.items():
#     print(k,v)


# print('dict')
# d1 = {}
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['c'] = 'C'
# d2 = {}
# d2['c'] = 'C'
# d2['b'] = 'B'
# d2['a'] = 'A'
# print(d1==d2)
# print('orderedDict:')
# d1 = collections.OrderedDict()####考虑元素增加的顺序
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['c'] = 'C'
# d2 = collections.OrderedDict()
# d2['c'] = 'C'
# d2['b'] = 'B'
# d2['a'] = 'A'
# print(d1==d2)####不同顺序创建的，所以是不相同的


import array
import binascii
import pprint

# a = array.array('i',range(3))####包括的操作分片、迭代以及向末尾增加元素
# print('Initial :',a)
# a.extend(range(3))
# print('Extend:',a)
# print('Slice  ：',a[2:5])
# print('Iterator:')
# print(list(enumerate(a)))

# def to_hex(a):#####不是很懂在干啥
#     chars_per_item = a.itemsize * 2
#     hex_version = binascii.hexlify(a)
#     num_chunks = len(hex_version) / chars_per_item
#     for i in range(int(num_chunks)):
#         start = i*chars_per_item
#         end = start + chars_per_item
#         yield hex_version[start:end]
# a1 = array.array('i',range(5))
# a2 = array.array('i',range(5))
# a2.byteswap()
# fmt = '%10s %10s %10s %10s'
# print(fmt % ('A1 hex','A1','A2 hex','A2'))
# print(fmt % (('-' * 10,) * 4))
# for values in zip (to_hex(a1),a1,to_hex(a2),a2):
#     print(fmt % values)


