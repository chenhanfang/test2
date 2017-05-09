#_*_ coding:utf-8 _*_
import matplotlib.pyplot as plt

#####折线图
# input_values=[1,2,3,4,5]
# squs=[1,4,2,16,25]
# plt.plot(input_values,squs,linewidth=5)
# plt.title('Square Numbers',fontsize=24)####标题
# plt.xlabel('Value',fontsize=24)####x坐标
# plt.ylabel('Square of Value',fontsize=14)####y坐标
# plt.tick_params(axis='both',labelsize=14)####设置刻度标记的大小
# plt.show()

######散点图
# x_values=[1,2,3,4,5]
# y_values=[1,4,2,15,35]
# plt.scatter(x_values,y_values,s=100)
# plt.title('Square Numbers',fontsize=24)
# plt.xlabel('x',fontsize=14)
# plt.ylabel('y',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()

######自动计算数据
# x_values1=list(range(1,1000))
# y_values1=[x**2 for x in x_values1]
# # plt.scatter(x_values1,y_values1,c=(0.54,0,0.8),edgecolors='none',s=40)######颜色的数字要小于1
# plt.scatter(x_values1,y_values1,c=y_values1,cmap=plt.cm.Reds,edgecolors='none',s=40)######渐变的颜色映射
# plt.title('Square Numbers',fontsize=24)
# plt.xlabel('x',fontsize=14)
# plt.ylabel('y',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.axis([0,1100,0,1100000])
# plt.show()

#####练习
# x_values1=[1,2,3,4,5]
# # x_values1=list(range(1,1000))
# y_values1=[x**3 for x in x_values1]
# # plt.scatter(x_values1,y_values1,c=(0.54,0,0.8),edgecolors='none',s=40)######颜色的数字要小于1
# plt.scatter(x_values1,y_values1,c=y_values1,cmap=plt.cm.Reds,edgecolors='none',s=40)######渐变的颜色映射
# plt.title('Square Numbers',fontsize=24)
# plt.xlabel('x',fontsize=14)
# plt.ylabel('y',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.axis([0,10,0,110])
# plt.show()

from random import choice
class Randomwalk():#######模拟随机漫步
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        self.values=[0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            if x_step == 0 and y_step == 0:
                continue
            next_x=self.x_values[-1] + x_step
            next_y=self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)



#####练习1
# rw=Randomwalk()
# rw.fill_walk()
# plt.scatter(rw.x_values,rw.y_values,c=(0.54,0,0.8),edgecolors='none',s=15)
# plt.show()
####练习2
while True:
    rw = Randomwalk(50000)######自定义设置的最大值
    # rw=Randomwalk()####默认设置的随机点数的最大值
    rw.fill_walk()
    # plt.figure(figsize=(10,6))######设置输出窗口尺寸
    # plt.figure(dpi=128,figsize=(10,8))#######设置分辨率，和窗口尺寸
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Greens,edgecolors='none', s=15)#####渐变颜色的散点图Red,Blue
    # plt.plot(rw.x_values, rw.y_values,linewidth=5, c='blue')######练习
    # plt.scatter(0,0,c='red',edgecolors='none',s=100)######设置起点颜色
    # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolors='none',s=100)#####设置重点颜色
    plt.axes().get_xaxis().set_visible(False)######影藏横坐标
    plt.axes().get_yaxis().set_visible(False)#####影藏纵坐标
    plt.show()
    # plt.savefig('hh.png',bbox_inches='tight')#######将生成的图片保存，第二个参数是去掉空白区域
    keep_running=input('make another walk?(y/n):')
    if keep_running == 'n':
        break
