import os


class fileCore ():
    def __init__(self, debug=0):
        self.debug = debug
        
    def query(self, path):
        if os.path.exists(path):
            return 1
        else:
            return 0

    def bundle(self):
        pass
    
    def fileCoreFileName(self):
        fileName = os.path.split(self.filePath)
        if self.debug: print 'the fileName : ' + fileName[1]

    def fileMayaLoc (self):
        mayaLoc = os.path.split(self.filePath)
        locDir = mayaLoc[0]
        if self.debug: print 'the locDir : ' + locDir
        return locDir