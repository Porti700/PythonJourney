import requests
import smtplib 
from email.message import EmailMessage
# API key (You must keep your api key private.)
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close()

## Mail password
pass_file = open("pass.txt", "r")
pass_key = pass_file.read()
pass_file.close()

# home address input
home = input("Enter a home address\n") 
  
# work address input
work = input("Enter a work address\n") 
  
# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
 
# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
  
# print the travel time
print("\nThe total travel time from home to work is", time)

# check if travel time is more than 1 hour
if (seconds > 3600):

    def email_alert(subject,body,to):
        msg=EmailMessage()
        msg.set_content(body)
        msg['subject']=subject
        msg['to']=to
    
        user="kevintest1233@gmail.com"
        msg['from']=user
        password=pass_key
        
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)
        server.quit()
    
if __name__ =='__main__':
    email_alert(f"Hey","hola ahora llegare tarder al trabajo, llegare a las {time}","kevinportillo11@gmail.com")
    print(f"Ya que te tardas {time} enviamos correo a tu jefe")