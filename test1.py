import os
from os import getcwd

print ("This is my current directory :", os.getcwd())



for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    #print(f"Currently in directory: {dirpath}")
    print(f"  Subdirectories: {dirnames}")
    #print(f"  Files: {filenames}")
    print("-" * 40)

current_path=os.getcwd()
new_dir="test"
file_name="file1"
full_new_path=os.path.join(current_path,new_dir)

try:
    if not os.path.exists(full_new_path):
        os.mkdir(full_new_path)
        print("New dir created fine with path :" , "{x}".format(x=full_new_path))
        open(file_name,"a").close()
        if os.path.isfile(file_name):
            print("File exists:", file_name)
        else:
            print("File does not exist:", file_name)
    else:
        print("Directory already exists:", full_new_path)
except Exception as e :
    print("Error While creating directory :", e)

os.chdir(current_path)
print(getcwd())
os.rmdir(full_new_path)
