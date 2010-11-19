import maya.cmds as cmds
import file
reload(file)

class fileMaya (file.File):
    def __init__(self, debug=0):
        self.debug = debug
        
    def fileMayaCurrentPath(self):
        currentPath = cmds.file(q = True, exn = True)
        if self.debug: print 'currentPath : ' + currentPath
    

    
