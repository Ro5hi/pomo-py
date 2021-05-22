import time

#timer 
def timer(t):
    while t: 
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1 
        print("Pomodoro!")
    t = input("Enter time time needed in seconds: ")
    
    timer(int(t))

# pomodoro    
def pomo():
    print("Starting pomodoro.")
    for i in range(4):
        t = 25*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(" " + timer, end="\r")
            time.sleep(1)
            t -= 1
        print("Take a break!")
        t = 5*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1 
        print("Back to work!")
        
    pomo()