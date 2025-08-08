# img=open('read.txt','r') #default mode is read
# #img.write("and my age is 21") 
# print(img.readline())
# img.close()

#a - Appends at the end of file
#r - Reads file
#w- Creates file if not existing and lets us write(But discards previously written texts)
#x- Creates a new file fails if exist



#CRUD mini-proj

from pathlib import Path
import os

def readfilenfolder():
    folder = input("Enter folder path (or press Enter for current): ").strip() or '.'
    path = Path(folder)
    if not path.exists():
        print("Folder doesn't exist!")
        return None
    items = list(path.rglob("*"))
    if not items:
        print("No files or folders found.")
    else:
        for i, item in enumerate(items):
            print(f"{i+1} : {item}")
    return path  # return Path object for later use


def createfile():
    folder_path = readfilenfolder()
    if not folder_path:
        return
    try:
        name = input("Enter your file name: ")
        p = folder_path / name  # file inside chosen folder
        print("1. Just create empty file\n2. Create file and write your thoughts")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            with open(p, 'x'):
                pass
            print("File created successfully")
        elif ch == 2:
            with open(p, 'w') as fw:
                data = input("Write your thoughts: ")
                fw.write(data)
                print("File created successfully")
        else: 
            print("File did not created successfully")
    except FileExistsError:
        print("File already exists!")
    except Exception as err:
        print(f"ERROR: {err}")


def readfile():
    folder_path = readfilenfolder()
    if not folder_path:
        return
    try:
        name = input("Enter your file name: ")
        p = folder_path / name
        if p.exists() and p.is_file():
            with open(p, 'r') as fr:
                print(fr.read())
            print("File read successfully")
        else:
            print("File doesn't exist")
    except Exception as err:
        print(f"ERROR: {err}")


def updatefile():
    folder_path = readfilenfolder()
    if not folder_path:
        return
    try:
        name = input("Enter your file name: ")
        p = folder_path / name
        print("1. Append lines\n2. Overwrite previous lines")
        ch = int(input("Enter your choice: "))
        if p.exists() and p.is_file():
            if ch == 1:
                with open(p, 'a') as fa:
                    data = input("Write your thoughts: ")
                    fa.write(data)
            elif ch == 2:
                with open(p, 'w') as fw2:
                    data = input("Write your thoughts: ")
                    fw2.write(data)
            print("File updated successfully")
        else:
            print("File doesn't exist")
    except Exception as err:
        print(f"ERROR: {err}")


def deletefile():
    folder_path = readfilenfolder()
    if not folder_path:
        return
    name = input("Enter file name: ")
    p = folder_path / name
    if p.exists() and p.is_file():
        try:
            os.remove(p)
            print("File deleted successfully")
        except Exception as err:
            print(f"ERROR: {err}")
    else:
        print("File doesn't exist")


print("1. Create file\n2. Read file\n3. Update file\n4. Delete file")
check = int(input("Enter choice: "))
if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Incorrect choice")
