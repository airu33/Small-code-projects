import os
from time import sleep
import shutil
from shutil import copy2 

loopTime = 3 # input time in seconds
src =  # The folder you whant to copy
dst =  # The folder you whant to paste to


# Prints time that is left until folder is copied
def PrintTime(t):
    mins, secs = divmod(t, 60)
    curentTime = f"{mins:02d}:{secs:02d}"
    print(curentTime, end="\r")

# Checks if folder alredy exists, if it exists delete it
def DeleteOldFolder():
    if os.path.exists(dst): 
        shutil.rmtree(dst)
        print("Existing folder removed")
    else:
        print("No existing folder found")

def main(t):
    while True:
        PrintTime(t)

        sleep(1)
        t -= 1
        
        if t == 0:  # When the time ends
            DeleteOldFolder()
            shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)   
            print("copied " + src + " pasted at " + dst)
            t = loopTime # Reset loop
            

# call function
if __name__ == '__main__':
    try:
        main(int(loopTime))   
    except KeyboardInterrupt(): # CTRL + C
        exit()
    