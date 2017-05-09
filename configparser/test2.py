import configparser
config=configparser.ConfigParser()
with open('test2.cfg','r') as cfgfile:
    config.readfp(cfgfile)
    name=config.get("info","name")
    age=config.get("info","age")
    print(name)
    print(age)
    config.set("info","sex",'male')
    config.set('info','age','54')
    age=config.getint("info",'age')
    print(name)
    print(type(age))
    print(age)
