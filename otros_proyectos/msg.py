import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    
    user="kevintest1233@gmail.com"
    msg['from']=user
    password="ujwsfdithudwbptr"
    
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
    
if __name__ =='__main__':
    email_alert("Hey","SOy kevin el 24 de agosto","kevinportillo11@gmail.com")