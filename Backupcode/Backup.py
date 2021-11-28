import os
import time
import shutil
from shutil import copy2 

time = 3 # input time in seconds


def main(time):

    src =  # The folder you whant to copy
    dst =  # The folder you whant to paste to

    while timer: # The countdown. it takes t integer in seconds.
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time -= 1 

        if time == 0:   # When the timer ends

            if os.path.exists(dst): # Checks if the folder alredy exists, if it exists delete it 
                shutil.rmtree(dst)
                print("Existing folder removed")
            else:
                print("No existing folder found")

            if os.path.exists(dst) == False:  # copies the src folder and paste it in dst folder
                shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)   
                print("New file pasted")
                print("copied " + src + " pasted at " + dst)
                time = 3 # If you whant it to loop
            else:
                print("Folder does not exist")
            

# call function
if __name__ == '__main__':
    try:
        main(int(time))   
    except KeyboardInterrupt(): # CTRL + C
        exit()
    