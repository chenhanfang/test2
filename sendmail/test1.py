import smtplib
from email.mime.text import MIMEText
from email.header import Header
smtpserver='smtp.163.com'
user='chfan1028@163.com'
password='777chf10287'
sender='chfan1028@163.com'
receiver='1751773456@qq.com'
subject='python email test'
msg=MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['subject']=Header(subject,'utf-8')
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()