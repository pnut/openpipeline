import maya.cmds as cmds
import file
reload(file)

class fileMaya (file.File):
    def __init__(self, debug=0):
        self.debug = debug
        
    def fileMayaCurrentPath(self):
        currentPath = cmds.file(q = True, exn = True)
        if self.debug: print 'currentPath : ' + currentPath
    
    #Returns the name of the currently opened file. ##pyapor##
    def mayaFileName(self):
        filePath = self.myFilePath()
        Path = os.path.split(filePath)
        fileName = Path[1]
        return fileName
        if self.debug: print fileName
        
    #Returns folder where currently opened file lives. ##pyapor## 
    def mayaLoc(self):
        loc = self.myFilePath()
        if self.debug: print loc
        locPath = os.path.split(loc)
        locDir = locPath[0]
        if self.debug: print locDir
        return locDir
    
    def mayaSave(self):
        fileSave = cmds.file(s = True)
        if self.debug: print fileSave + ' has been saved.'
    
    #What it does is pretty much rename and save. ##pyapor##
    def mayaSaveAs(self, folderPath, name):
        if self.debug: print name
        if self.debug: print folderPath
        renamePath = os.path.join(Path, name)
        if self.debug: print renamePath 
        
        if self.query(renamePath):
            if self.debug: print 'File name already existis'    
        else:
            cmds.file(rn = renamePath)
            self.mySave()
            if self.debug: print 'File has been renamed to ' + self.newName
    
    #Starts a new file but gives you the option to either save the current scene or not to do so. ##pyapor##
    def mayaNew(self, bool=0):
        if bool == 1:
            self.mysave()
            cmds.file(new = True, f = True)
        else:
            cmds.file(new = True, f = True)
    
