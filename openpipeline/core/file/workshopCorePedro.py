import os

import file
reload(file)

class Workshop(file.File):
    def __init__(self):
        pass
    
    def open(self, path, item, version):
        # break out workshop
        name = '%(item)s_workshop_%(version)04d.mb' % {'item': item, "version": version}     
        workshopPath = os.path.join(path, "workshop", name)
                
        if self.query(workshopPath):
            print workshopPath
            return workshopPath
        else:
            print "error"
    
    #Returns whether the worskshop folder is empty or not. ##pyapor##
    def queryDir(path):
        self.workshopFolder = os.path.join(path, "workshop")
        dirList = os.listdir(workshopFolder)
        if dirList == [] :
            return True
        else:
            return False
        
    #Brings back a list of all of th workshop files in the workshop folder... this could probably be used later on to check if any files are missing. ##pyapor##  
    def queryDirList(path):
        self.workshopFolder = os.path.join(path, "workshop")
        dirList = os.listdir(workshopFolder)
        if dirList == [] :
            return False
        else:
            return dirList
    
    #Moves one branch up the file path. ##pyapor##
    def upDir(self, filePath):
        filePath = os.path.split(filePath)
        folderPath = filePath[0]
        return folderPath
    
    #Returns the the file path of the workshop that needs to be saved. Do you prefer to return the whole path or just the renamed workshop filename? ##pyapor##
    def saveWorkshop(self, name, folderPath):
        if self.queryDir(folderPath):
            fileNum = 1
            #I think that hardcoding the "workshop" into the filename is appropriate in this case. 
            workshopName = name + "workshop" + fileNum.zfill(4)
            if self.debug: print workshopName
            workshopFileName = os.path.join(path, workshop, workshopName)
            if self.debug: print workshopFileName
        else:
            self.renameIncremental(name, folderPath)
            
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