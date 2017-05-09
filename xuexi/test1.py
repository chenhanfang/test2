
# alien_0={'x_position':0,'y_position':25,'speed':'medium','points':'5'}
# print('original x_position:'+str(alien_0['x_position']))
# print(alien_0)

# if alien_0['speed']=='slow':
#     x_increment=1
# elif alien_0['speed']=='medium':
#     x_increment=2
# else:
#     x_increment=3
# alien_0['x_position']=alien_0['x_position']+x_increment
# print('new x_position:'+str(alien_0['x_position']))
# del alien_0['points']
# print(alien_0)
# print('alien is %s'%alien_0['speed'].upper()+'.')

# person={'first_name':'chen','last_name':'han','age':20,'city':'hangzhou'}
# print(person)
#
# #不能获取int型的数据
# for key,value in person.items():
#     print('\nkey:'+key)
#     print('value:'+value)

# favorite_languages={
#     'jen':'python',
#     'sarach':'c',
#     'edward':'ruby',
#     'phil':'python',
# }

# for name,language in favorite_languages.items():
#     print(name.title()+"'s favorite language is "+ language.title()+ '.')

# for name in favorite_languages.keys():
#     print(name.title())

# friends=['phil','sarach']

# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print('hi'+name.title() +',i see your favorite language is '+
#               favorite_languages[name].title()+'!')
# #
# if 'erin' not in favorite_languages.keys():
#     print('Erin,please take our poll')
#
# for name in sorted(favorite_languages.keys()):
#     print(name.title()+",thank you for taking the poll.")
# print('the following languages have been mentioned:')
# # for language in favorite_languages.values():#没有去重的遍历
# for language in set(favorite_languages.values()):#去重的遍历
#     print(language.title())


# rivers={'nile':'egypt','changjiang':'china','meigong':'taiguo'}
# for river,country in rivers.items():
#     print('the '+ river.title()+' run through '+country.title())
#
# for river in rivers.keys():
#     print(river.title())
#
# for country in rivers .values():
#     print(country.title())


# alien_0={'color':'green','points':'5'}
# alien_1={'color':'yellow','points':'10'}
# alien_2={'color':'red','points':'15'}
# aliens=[alien_0,alien_1 ,alien_2 ]
# for alien in aliens:
#     print(alien)

# aliens=[]
# for alien_number in range(30):
#     new_alien={'color':'green','point':5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print('.......')
# print('total number of aliens:'+str(len(aliens)))
#
# from random import choice
# import random
# color=['blue','orange','pink']
# for alien in aliens:
#     if alien['color']=='green':
#         alien['color']=choice(color)###随机获取数据字典中的数据
#         alien['point']=10
#         alien['speed']='medium'
#     elif alien['color']=='yellow':
#         alien['color']='red'
#         alien['point']=15
#         alien['speed']='fast'
# for alien in aliens:
#     print(alien)
# print('.......')
# print('...............')
# import random
# list=[1,2,3,2,4,6,8,7,9,10]
# slist=random.sample(list,5)####从列表中随机获取一组元素
# print(slist)
# print(list)
# print('..................')

# pizza={'crust':'thick','toppings':['mushrooms','extra cheese'],}
# print('you ordered a'+ pizza['crust']+'-crust pizza '+'with the following toppings:')
# for topping in pizza['toppings']:
#     print('\t'+topping)

# favorite_languages1={'jen':['python','ruby'],'sarah':['c'],'edward':['ruby','go'],'phil':['python','haskell'],}
# for name,languages in favorite_languages1.items():
#     print('\n'+name.title()+"'s favorite languages are:")
#     for language in languages:
#         print('\t'+language.title())####\t缩进；\n分行


# users={
#     'aeinstein':{
#         'first':'albert',
#         'last':'einstein',
#         'location':'princeton',
#     },
#     'mcurie':{
#         'first':'marie',
#         'last':'curie',
#         'location':'paris',
#     },
# }
# for username,user_info in users.items():
#     print('\nUsername:'+username)
#     full_name=user_info['first']+' '+user_info['last']
#     location=user_info['location']
#     print('\tFull name:'+full_name.title())
#     print('\tLocation:'+location.title())

# favorite_places={'chen':['hangzhou','shanghai','beijing'],'wang':['guangzhou','shengzhemg'],'ding':['hefei','shanghai'],}
# for name,cities in favorite_places.items():
#     print(name.title()+"'s favorite city are:")
#     for city in cities:
#         print('\t'+city.title())

# message=input('tell me something,and i will repeat it back to you:')
# print(message)

# name=input('plaese enter your name:')
# print('hello,'+name+'!')

# age=input('how old are you?')

# height=input('how tall are you ,in inches?')
# height=int(height)
# if height >= 36:
#     print("\nyou're tall enough to ride!")
# else:
#     print("\nyou'll be able to ride when you're a little older.")

# number=input("enter a number,and i'll tell you if it's even or odd:")
# number=int(number)
# if number % 2 == 0:
#     print('\nthe number '+str(number)+' is even.')
# else:
#     print('\nthe number '+str(number)+' is odd.')


# car=input('let me see if i can find you a sunbaru:')
# print(car)

# numbers=input('how many person in you:')
# numbers=int(numbers)
# if numbers > 8:
#     print("\nthere don't have tables!")
# else:
#     print('\nthere have tables')

# number=input('please enter a number:')
# number=int(number)
# if number % 10 ==0:
#     print('this number is right')
# else:
#     print('this number is wrong')

# current_number=1
# while current_number <=5:
#     print(current_number)
#     current_number+=1

# prompt='\ntell me somethong,and i will repeat i back to you:'
# prompt+='\nenter "quit" to end the program.'
# message=''
# while message !='quit':
#     message=input(prompt)
#     print(message)

# active=True
# while active:
#     message=input(prompt)
#
#     if message=='quit':
#         active=False
#     else:
#         print(message)


#break用法
# prompt1='\nplease enter the name of a city you have visited:'
# prompt1+="\n('enter 'quit' when you are finished.）"
# while True:
#     city=input(prompt1)
#     if city=='quit':
#         break
#     else:
#         print("i'd love to go to "+city.title()+"!")


#continue用法
# current_number=0
# while current_number<10:
#     current_number+=1
#     if current_number % 2==0:####条件满足就跳出循环
#         continue
#     print(current_number)


# prompt2='\nni xu yao fang na zhong tiao liao:'
# prompt2+='\n(when enter quit you are finished)'
#
# while True:
#     tiaoliao=input(prompt2)
#     if tiaoliao =='quit':
#         break
#     else:
#         print('wo men hui fang tiaoliao:'+tiaoliao.title()+'!')


# 练习
# prompt3='\n ni de nian ling shi duo shao:'
# prompt3+=''
# while True:
#     age=input(prompt3 )
#     if age=='quit':
#         break
#     age=int(age)
#     if age < 3:
#         print('you are free.')
#     elif age <12:
#         print('you need pay for 10$.')
#     else:
#         print('you need pay for 15$.')

# # #在列表之间移动元素
# unconfirmed_users=['alice','brain','candace']
# confirmed_users=[]
# while unconfirmed_users:
#     current_user=unconfirmed_users.pop()####可删除末尾元素，并可以接着使用
#     print('verifying.user:'+current_user.title())
#     confirmed_users .append(current_user)
# print("\nthe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user .title())


# #删除包含特定值
# pets=['dog','cat','cat','goldfish','cat','rabbit']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

##使用用户输入填充字典
# responses={}
# polling_active=True
# while polling_active:
#     name=input('\nwhat is your name?')
#     response=input('which mountain would you like to climb someday?')
#     responses[name]=response
#     repeat=input('would you like to let another person respond?(yes/no)')
#     if repeat=='no':
#         polling_active=False
# print('\n----poll results----')
# for name,response in responses.items():
#     print(responses)
#     print(name+' would like to climb '+response+'.')

# #练习
# sandwich_orders=['sand1','wich1','order1']
# finished_sandwiches=[]
# while sandwich_orders:
#     sandwich=sandwich_orders .pop()
#     print('verifying sandwich:'+sandwich.title())
#     finished_sandwiches.append(sandwich )
# print('\nthe following sandwich have been confirmed:')
# for finished_sandwiche in finished_sandwiches:
#     print(finished_sandwiche.title())

# # 练习
# sandwich_orders=['pastrami','sand','pastrami','wich1','pastrami','order1','order1']
# print('\npastrami have been saved.')
# while 'pastrami' in sandwich_orders :
#     sandwich_orders .remove('pastrami')
# print(sandwich_orders)

# # 练习
# visiters={}
# polling_active=True
# while polling_active:
#     name=input('\nwhat is your name?')
#     visiter=input('if you could visit one place in the world,where would you go?')
#     visiters[name]=visiter
#     repeat=input('would you like to let another person respond?(yes/ no)')
#     if repeat == 'no':
#         polling_active=False
# print('\n------poll results-----')
# for name,visiter in visiters .items():
#     print(name+' would like to visit '+visiter +'.')

# # 函数
# def greet_user():
#     print('hello!')
# greet_user()

# def greet_user(username):
#     print('hello,%s!'%username.title())
# greet_user('chen')

# def display_message(xuexi):
#     print('xuexile:%s.'%xuexi)
# display_message('math')

# def favorite_book(book):
#     print('one of my favorite books is %s'%book.title())
# favorite_book('gone with wind')

# def describe_pet(animal_type,pet_name):
#     print('\ni have a %s .'%animal_type)
#     print("my "+animal_type+"'s name is %s."%pet_name.title())
# describe_pet('hhhh','xxxx')
# describe_pet(animal_type='xxx',pet_name='hhh')

# def describe_pet(pet_name,animal_type='dog'):
#     print('\ni have a %s.'%animal_type)
#     print('my '+animal_type+"'s name is %s."%pet_name.title())
# describe_pet(pet_name='xxx')
# describe_pet('willie')
# describe_pet('harry','hamster')
# describe_pet(pet_name='harry',animal_type='hamster')
# describe_pet(animal_type='hamster',pet_name='harry')

# def make_shirt(size,simple='i love python'):
#     print('\ni have a %s shirt.'%size)
#     print('my '+size+' shirt has %s on it.'%simple.title())
# make_shirt('m')

# def get_formatted_name(first_name,last_name):
#     full_name=first_name+' '+last_name
#     return full_name.title()
# musician=get_formatted_name('jimi','hendrix')
# print(musician)

# def get_formatted_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name=first_name+' '+middle_name+' '+last_name
#     else:
#         full_name=first_name+' '+last_name
#     return full_name.title()
# musician1=get_formatted_name('jimi','lee','hendrix')
# musician2=get_formatted_name('jimi','hendrix')
# print(musician1)
# print(musician2)

# def build_person(first_name,last_name):
#     person={'first':first_name,'last':last_name}
#     return person
# musician3=build_person('jimi','hendrix')
# print(musician3 )

# def build_person1(first_name,last_name,age=''):
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#     return person
# musician4=build_person1('jimi','hendrix',age=27)
# print(musician4 )

# def get_formatted_name(first_name,last_name):
#     full_name=first_name+' '+last_name
#     return full_name.title()
# while True:
#     print('\nplease tell me your name:')
#     print("(enter 'q' at any time to quit)")
#     f_name=input('first name:')
#     if f_name == 'q':
#         break
#     l_name=input('last name:')
#     if l_name == 'q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print('\nhello,'+formatted_name +'!')

# def city_country(city,country):
#     full_name=city+','+country
#     return full_name.title()
# ct1=city_country('santiago','chile')
# ct2=city_country('hangzhou','china')
# ct3=city_country('mangu','taiguo')
# print(ct1)
# print(ct2)
# print(ct3)

# def make_album(singer,albums,shuliang=''):
#     album={'singer':singer,'albums':albums}
#     if shuliang:
#         album['shuliang']=shuliang
#     return album
# album1=make_album('zhoujielun','chuangbiangushi',shuliang=10)
# album2=make_album('zhh','dhjdk')
# print(album1)
# print(album2)

# def make_album(singer,album):
#     album={'singer':singer,'album':album}
# while True:
#     print("(enter 'q' at any time to quit)")
#     singer=input('\nplease send singer name:')
#     if singer == 'q':
#         break
#     album=input('please send album name:')
#     if album == 'q':
#         break
#     make_album1=make_album(singer,album)
#     print('\n'+singer+"'s album is "+album+'.')


# def greet_users(names):
#     for name in names:
#         msg='hello,'+name.title()+"!"
#         print(msg)
# usernames=['hhhhh','try','mahd']
# greet_users(usernames)

# unprinted_designs=['iphone case','robot pendant','dodecahedron']
# completed_models=[]
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print('printing models:'+current_design)
#     completed_models .append(current_design)
# print('\nthe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model )


def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print('printing model:'+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print('\nthe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

