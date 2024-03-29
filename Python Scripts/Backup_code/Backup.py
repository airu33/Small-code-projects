import os
import shutil
from time import sleep

print("Press Ctrl + C to stop the program")

print("loopTime is the amount of seconds between copies")
loopTime = int(input("Numbers only: ")) # input time in seconds

print("src is the sorce file you whant to copie example C:/Users/Name/Desktop/Folder")
src = input(": ") # The folder you whant to copy

print("dst is the destination folder you whant to copie to example C:/Users/Name/Desktop/Folder")
dst = input(": ") # The folder you whant to paste to


# Prints time that is left until folder is copied
def PrintTime(t):
    mins, secs = divmod(t, 60)
    curentTime = f"{mins:02d}:{secs:02d}"
    print(curentTime, end="\r") # Prints out the time left in one row. end=\r does not spam the terminal window

# Checks if folder alredy exists, if it exists delete it
def DeleteOldFolder():
    if os.path.exists(dst): 
        shutil.rmtree(dst) #Removs dst folder
        print("Existing folder removed")
    else:
        print("No existing folder found")

def main(t):
    sleep(1)
    

    while True:
        PrintTime(t)

        sleep(1)
        t -= 1
        # When the time ends check if dst folder exist and copies the src folder
        if t == 0:  
            DeleteOldFolder()
            shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
            print("copied " + src + " pasted at " + dst)
            t = loopTime # Reset loop
            

# call function
if __name__ == '__main__':
    try:
        main(int(loopTime))   
    except KeyboardInterrupt(): # CTRL + C
        exit()
    