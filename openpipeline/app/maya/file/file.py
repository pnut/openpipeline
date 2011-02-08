import maya.cmds as cmds
import core.file.file as file
reload(file)
 

class FileMaya (file.FileCore):

    def __init__(self, debug=0):
        self.debug = debug
        if self.debug: print 'FileMaya init'
        
    def mayaOpen(self, filePath, bool=0):
        if bool:
            self.mayaSave()
            fileSaved = cmds.file(filePath, open = True)
        else:
            fileSaved = cmds.file(filePath, force = True, open = True)
        if self.debug: print filePath + ' has been saved.'
        return filePath
           
    def mayaCurrentPath(self):
        currentPath = cmds.file(q = True, exn = True)
        if self.debug: print 'currentPath : ' + currentPath
        return currentPath
    
    #Returns the name of the currently opened file. ##pyapor##
    def mayaFileName(self):
        filePath = self.mayaCurrentPath()
        Path = os.path.split(filePath)
        fileName = Path[1]
        if self.debug: print fileName
        return fileName
        
        
    def mayaSave(self):
        fileSave = cmds.file(s = True)
        if self.debug: print fileSave + ' has been saved.'
        return
    
    #What it does is pretty much rename and save. ##pyapor##
    def mayaSaveAs(self, folderPath, name):
        if self.debug: print name
        if self.debug: print folderPath
        renamePath = os.path.join(Path, name)
        if self.debug: print renamePath 
        #Checking if the new file path already exists. ##pyapor##  
        if self.query(renamePath):
            if self.debug: print 'File name already existis'    
        else:
            cmds.file(rn = renamePath)
            if self.debug: print 'File has been renamed to ' + self.newName
            self.mySave()
    
    #Starts a new file but gives you the option to either save the current scene or not to do so. ##pyapor##
    def mayaNew(self, bool=0):
        if bool == 1:
            self.mayaSave()
            cmds.file(new = True, f = True)
        else:
            cmds.file(new = True, f = True)
            return
#!/usr/bin/env python

