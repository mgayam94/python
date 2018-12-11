import time
from datetime import datetime as dt

hosts_temp=r"D:\Dropbox\pp\block_websites\Demo\hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts" #file path of hosts.
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"] #these are the websites to be blocked.

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): #condition to check the time between 8.00am to 04.00pm
        print("Working hours...")
 #code below helps to open the file and perform the actions.
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5) #used to run the code for every 5sec.
