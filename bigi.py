import os,platform
os.system('git pull')

bigi=platform.architecture()[0]
if bigi=="32bit":
    print('Sorry Update Your Phone...')
elif bigi=="64bit":
    __import__("bn").reg()
