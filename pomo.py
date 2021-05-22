import time

t = int(input("How much time do you want to set?"))

while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{0:2d}'.format(mins, secs)

    print(timer, end="\r") 
    time.sleep(1)
    t -= 1    
    print('Rest time!')