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
    
    #Returns the filename from a file path. ##pyapor## ##jum##
    def fileCoreFileName(self):
        fileName = os.path.split(self.filePath)
        if self.debug: print 'the fileName : ' + fileName[1]

    #Moves one branch up the file path. ##pyapor## ##jum##  
    def fileCoreLoc(self):
        fileCoreLoc = os.path.split(self.filePath)
        locDir = mayaLoc[0]
        if self.debug: print 'This file is located in: ' + locDir
        return locDir
    
    #Returns whether a folder is empty or not. ##pyapor##
    def fileCoreQueryDir(self, folderPath):
        dirList = os.listdir(folderPath)
        if dirList == [] :
            if self.debug: folderPath + " is empty."
            return True
        else:
            if self.debug:
                dirList = self.queryDirList()
                print ('The list of files in ' + folderPath + ' is ' + dirList + '.')
            return False
    
    #Brings back a list of all of the files in a folder... this could probably be used later on to check if any files are missing. ##pyapor##  
    def fileCoreQueryDirList(self, folderPath):
        Folder = os.path.join(path, folderPath)
        dirList = os.listdir(Folder)
        if dirList == [] :
            return False
        else:
            if self.debug: print dirList
            return dirList