import shutil
import os

os.getcwd()
os.mkdir("Practical4")

source="C:/Users/goluk/Desktop"
item_list=os.listdir(source)
print(item_list)

# spliting the text
path_1="C:/Users/goluk/Desktop/coding class/Alkatra-VariableFont_wght.ttf"
root, extension=os.path.splitext(path_1)
print("the root element are: ", root)
print("the extension is:" , extension)

# making a copy of file
source="C:/Users/goluk/Desktop/coding class/Alkatra-VariableFont_wght.ttf"
destination="C:/Users/goluk/Desktop/python classec"
out_put = shutil.copy(source,destination)
print("the file has copied sucessfuly !!")


# doubt root, extension (line no 13 ) are pre defined or it's a variable.













