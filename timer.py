import time
from playsound import playsound
def countdown_timer(seconds):
    while seconds > 0 :
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds -=1
    print('timer')
playsound('mixkit-sound.wav')
seconds = input("Enter the time in no.of seconds")
countdown_timer(int(seconds))    