import os
import shutil

sourcepath = 'C:/Users\Dwaipayan Munshi\Downloads'
sourcefiles = os.listdir(sourcepath)
destinationpath = 'F:/Projects\Personal\DataSetsMerger'
for file in sourcefiles :
    if file.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,file),os.path.join(destinationpath,file))
        
