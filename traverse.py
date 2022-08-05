import os
from os.path import abspath,join,getsize

i=0
for top_dir,directories,files in os.walk("."):
    for _file in files:
        if i<20:
            fullpath=abspath(join(top_dir,_file))
            print(fullpath)
            i+=1

#extract file size>10Kb
sizes=[]
for top_dir,directories,files in os.walk("."):
    for _file in files:
        fullpath=abspath(join(top_dir,_file))
        size=getsize(fullpath)
        if size>10:
            sizes.append(join(fullpath, ' ', str(size), '\n'))
print(sizes)
