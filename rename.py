import os

path = ""
newName = ""

for file in os.listdir(path):
    res = file.split("@")
    end = res[0].split(".")
    new = file.replace(end[0], newName)
    os.rename(os.path.join(path,file),os.path.join(path, new))
