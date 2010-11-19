import os

class File:
    def __init__(self, debug=0):
        self.debug = debug
  
    def query(self, path):
        if os.path.exists(path):
            return 1
        else:
            return 0

    def bundle(self):
        pass
    
     #Returns whether a folder is empty or not. ##pyapor##
    def queryDir(self, folderPath):
        dirList = os.listdir(folderPath)
        if dirList == [] :
            return True
        else:
            return False
    
    #Brings back a list of all of the files in a folder... this could probably be used later on to check if any files are missing. ##pyapor##  
    def queryDirList(self, folderPath):
        Folder = os.path.join(path, folderPath)
        dirList = os.listdir(Folder)
        if dirList == [] :
            return False
        else:
            if self.debug: print dirList
            return dirList
    
    #Returns the filename path incrementally named according to the list of files in the folder, this is specifically for workshop renaming ##pyapor##
    def renameIncremental(self, name, folderPath):
        workshopList = self.quieryDirList(folderPath)
        workshopLen = len(workshopList)
        lastWorkshop = workshopList[workshopLen]
        if self.debug: print lastWorkshop
        workshopFileName = os.path.splitext(lastWorkshop)
        workshopFileNumber = workshopFileName[2]
        workshopFileNumber = workshopFileNumber ++ 1
        workshopFileNumber = str(workshopFileNumber)
        workshopFileName = name + "_workshop_" + workshopFileNumber.zfill(4)
        workshopPath = os.path.join(path, "workshop", workshopFileName)
        if self.debug: print workshopPath
        return workshopPath
    
    #Returns the the file path of the workshop that needs to be saved. Do you prefer to return the whole path or just the renamed workshop filename? ##pyapor##
    def saveRenameWorkshop(self, name, folderPath):
        if self.queryDir(folderPath):
            fileNum = 1
            #I think that hardcoding the "workshop" into the filename is appropriate in this case. 
            workshopName = name + "workshop" + fileNum.zfill(4)
            if self.debug: print workshopName
            workshopFileName = os.path.join(path, workshop, workshopName)
            if self.debug: print workshopFileName
        else:
            self.renameIncremental(name, folderPath)