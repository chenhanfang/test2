#coding=utf-8
import configparser
conf=configparser.RawConfigParser()####生成config对象
conf.read('test.cfg')
sections=conf.sections()
print('sections:%s'%sections)
options=conf.options('sec_a')######得到指定section的所有option
print('options:%s'%options)
kvs=conf.items('sec_a')########得到指定section的所有键值对
print('sec_a:%s'%kvs)
str_val=conf.get('sec_a','a_key1')#######指定section,option读取值
int_val=conf.getint('sec_a','a_key2')
print('value for sec_a is a_key1:%s'%str_val)
print('value for sec_a is a_key2:%s'%int_val)

####写配置文件
conf.set('sec_b','b_key3','new-$r')####更新指定setion,option的值
conf.set('sec_b','c_newkey','new-value')######写入指定section增加新option和值
conf.add_section('b_new_section')####增加新的section
conf.set('b_new_section','new_key','new_value')
conf.write(open('test.cfg','w'))#######写回配置文件