import shutil
import os

from_dir="C:/Users/goluk/Downloads"
to_dir="C:/Users/goluk/Documents"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
     name,extension=os.path.splitext(i)
     print(name,extension)

     