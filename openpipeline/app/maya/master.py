import maya.cmds as cmds
import file
reload(file)

class masterMaya (file.File):
    def __init__(self, debug=0):
        self.debug = debug
        
    def masterOpen (path):
        fileOpen = cmds.file(path, f=True, o=True)
        if self.debug : print fileOpen + ' has been opened.'
    
    def masterSave (self):
        fileSave = cmds.file(s = True)
        if self.debug: print fileSave + ' has been saved.'
        

    