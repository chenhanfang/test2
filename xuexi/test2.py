# def make_pizza(size,*toppings):###传递任意数量的实参
#     print('\nmaking a %s-inch pizza with the following toppings:'%str(size))
#     for topping in toppings:
#         print('-'+topping)
# make_pizza(16,'pepperoni')
# make_pizza(13,'mushrooms','green peppers','extra cheese')

# def build_profile(first, last, **user_info):###使用任意数量的关键字实参
#     profile={}
#     profile['first_name']=first
#     profile['last_name']=last
#     for key,value in user_info.items():
#         profile[key]=value
#     return profile
# user_profile=build_profile('albert','einstein',
#                            location='princeton',
#                            field='physics')
# print(user_profile)

# def build_profile(first,last,**info):
#     profile={}
#     profile['firstname']=first
#     profile['lastname']=last
#     for key,value in info.items():
#         profile[key]=value
#     return profile
# def user_profile(*toppings):####练习
#     myinfo=build_profile('chen','han',age='hh',sex='nv',tall='iu')
#     print(myinfo)
#     print('\nni xu yao de shi cai shi:')
#     for topping in toppings:
#         print('-'+topping)
# user_profile('jj','jfdk','fjke')

def make_car(zhizuo,xinhao,**info):
    carfile={}
    carfile['zhizuo']=zhizuo
    carfile['xinhao']=xinhao
    for key,value in info.items():
        carfile[key]=value
    return carfile
car=make_car('subaru','outback',color='blue',two_package='ture')
print(car)


