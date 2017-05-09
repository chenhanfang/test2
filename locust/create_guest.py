f = open('guests.txt','w')
for i  in range(1,100):
    str_i = str(i)
    realname = 'han' + str_i
    phone = 17600000000 + i
    email = 'han' +str_i +'@163.com'
    sql = "INSERT INTO login_guest(realname,phone,email,sign,event_id) VALUES('"+realname+"',"+str(phone)+",'"+email+"',0,1 );"
    f.write(sql)
    f.write('\n')
f.close()