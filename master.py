import os, platform, time, win32api

#Current Operating System
os_platform = platform.system()

#Assumes master mic volume is not muted as this is usually handled on an app-to-app basis
#Also sets preset max mic volume to 100% which is updated later should theree be variation
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
            #For reference: https://www.codestudyblog.com/sf2002d/0223183122.html
            win32api.SendMessage(-1, 0x319, 0x30292, 0x0a * 0x10000)
            mute = 0
            time.sleep(2)
        else:
            win32api.SendMessage(-1, 0x319, 0x30292, 0x09 * 0x10000)
            mute = 1
            time.sleep(2)
