from random import randint
import pygal######创建图表
import matplotlib.pyplot as plt
class Die():
    def __init__(self,num_sides=6):
        self.num_sides =num_sides
    def roll(self):
        return randint(1,self.num_sides)

# die=Die()
# results=[]#####掷骰子生成结果
# for roll_num in range(1000):
#     result=die.roll()
#     results.append(result)
# # print(results)
#
# frequencies=[]#####对结果进行分析
# for value in range(1,die.num_sides+1):
#     frequency=results.count(value)
#     frequencies.append(frequency)
# # print(frequencies)
#
# hist=pygal.Bar()#####结果可视化
# hist.title='result of rolling one d6 1000 times.'
# hist.x_labels=['1','2','3','4','5','6']
# hist.x_title='result'
# hist.y_title='frequency of result'
# hist.add('d6',frequencies)
# hist.render_to_file('die_visual.svg')#######在浏览器中输入路径打开生成的条形图

die1=Die(8)
die2=Die()
x_values=[]
y_values=[]
for roll_num in range(1000):
    x_value=die1.roll()
    y_value=die2.roll()
    x_values.append(x_value)
    y_values.append(y_value)
plt.scatter(x_values,y_values,c=(0,0,0.9),edgecolors='none',s=10)
plt.show()