import os, platform, time

os_platform = platform.system()

mute = 0
preset = 100

#Linux 
if os_platform == 'Linux':
    preset = str(os.popen('amixer get Capture').readlines()[0])
    while True:
        if mute:
            os.system('amixer set Capture ' + preset +'%')
            mute = 0
            time.sleep(2)
        else:
            os.system('amixer set Capture 0%')
            mute = 1
            time.sleep(2)
#Mac
elif os_platform == 'Darwin':
    preset = str(os.popen('osascript -e "input volume of (get volume settings)"').readlines()[0])
    while True:
        if mute:
            os.system('osascript -e "set volume input volume ' + preset +'"')
            mute = 0
            time.sleep(2)
        else:
            os.system('osascript -e "set volume input volume 0"')
            mute = 1
            time.sleep(2)
#Windows
else:
     while True:
        if mute:
            print("Windows, muting")
            mute = 1
            time.sleep(2)
        else:
            mute = 0
            time.sleep(2)
