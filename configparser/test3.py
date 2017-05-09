import configparser
#######rawconfiparser支持ini文件读取类，
# configparser,safeconfigparser支持对%（value)s变量分析

# conf=configparser.RaWConfigParser()
# conf=configparser.ConfigParser()
conf=configparser.SafeConfigParser()
conf.read('test3.cfg')
print(conf.get("portal",'url'))
conf.set("portal",'url2','%(host)s:%(port)s')
print(conf.get('portal','url2'))