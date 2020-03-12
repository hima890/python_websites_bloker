import time
from datetime import datetime as dt

host_path = "/home/hima/Documents/hosts.txt"
redirect = '127.0.0.1'
websites_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com']
start = input('inter the start time: ')
end = input('inter the end time: ')
a = 5

print('you have 5 web sites you can block')
print('if you wish to end the web site intring press q' + ' ,' + 'the formating must be like www.exmple.com')

while a > 0:
    a = a - 1
    b = input('inter the web site domin: ')
    if b == 'q':
        print('the web site list is save')
        break
    else:
        websites_list.append(b)
        


dt1 = dt(dt.now().year, dt.now().month, dt.now().day, int(start))
dt2 = dt(dt.now().year, dt.now().month, dt.now().day, int(end))
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