#_*_ coding:utf-8 _*_
from nose.tools import nottest,istest,assert_equal,assert_in
from nose_ittr import IttrMultiplier
import requests,json,os

curr_dir = os.path.dirname(os.path.abspath(__file__))


class TestNewProductDetail(object):
    __metaclass__ =IttrMultiplier
    @istest
    @ittr(channels_txt_name=['channels.txt'],check_list_txt_name=['check_list.txt'])
    def test_check_channels(self):
        channels_txt_path=os.path.join(curr_dir,self.channels_txt_name)
        check_list_txt_path=os.path.join(curr_dir,self.check_list_txt_name)
        the_channels=[]
        with open(channels_txt_path) as channels:
            for line in channels.readlines():
                line=line.strip()
                if line != '':
                    the_channels.append(line)
        with open(check_list_txt_path) as check_list:
            check_items = check_list.readlines()
            for check_item in check_items:
                if check_item.strip() in the_channels:
                    pass
                elif check_item == '\n':
                    pass
                else:
                    print(check_item)