import platform, time

os_platform = platform.system()

mute = 0
preset = 100

#Linux 
if os_platform == 'Linux':
    while True:
        if mute:
            print("Linux, muting")
            mute = 0
            time.sleep(2)
        else:
            mute = 1
            time.sleep(2)
#Mac
elif os_platform == 'Darwin':
    while True:
        if mute:
            print("Mac, muting")
            mute = 0
            time.sleep(2)
        else:
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
