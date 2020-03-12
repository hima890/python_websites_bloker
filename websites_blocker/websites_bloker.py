import time
from datetime import datetime as dt

host_path = "/etc/hosts"
redirect = '127.0.0.1'
websites_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com']


dt1 = dt(dt.now().year, dt.now().month, dt.now().day, 7)
dt2 = dt(dt.now().year, dt.now().month, dt.now().day, 16)
while True:
    if (dt1 < dt.now()) and (dt.now() < dt2) :
        print('working huors....')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if  not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
                      
        print('Fun hours....')
    time.sleep(5)