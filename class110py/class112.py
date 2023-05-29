import os
import shutil
source="C:/Users/goluk/Downloads"
destination="C:/Users/goluk/Desktop"
list =os.listdir(source)
for i in list:
    name,extension=os.path.splitext(i)
    print(name,extension)
    if extension=="":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1=source + "/" + i
        path2=destination + "/" + "image"
        path3=destination + "/" + "image" + "/" + i
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
             os.makedirs(path2)
             print("moving")
             shutil.move(path1,path3)
        
# ask from teacher to re-explain this code from line no 9.
# name, extension (line no 7) are pre define or a variable created by us.


