import grequests
urls=[
    'http://www.baidu.com',
    'http://github.com',
    'http://www.xdaili.cn',
]
rs=(grequests.get(u) for u in urls)
grequests.map(rs)

