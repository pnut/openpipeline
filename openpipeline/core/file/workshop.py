import os

import file
reload(file)

class Workshop(file.File):
    def __init__(self, debug=0):
        self.debug = debug
    
    def open(self, path, item, version):
        # break out workshop
        name = '%(item)s_workshop_%(version)04d.mb' % {'item': item, "version": version}     
        workshopPath = os.path.join(path, "workshop", name)
                
        if self.query(workshopPath):
            print workshopPath
            return workshopPath
        else:
            print "error"
    
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
        filePath = os.path.join(path, "workshop", workshopFileName)
        return filePath
        if self.debug: print filePath
    
    #Returns the the file path of the workshop that needs to be saved. Do you prefer to return the whole path or just the renamed workshop filename? ##pyapor##
    def saveWorkshop(self, name, folderPath):
        if self.queryDir(folderPath):
            fileNum = 1
            #I think that hardcoding the "workshop" into the filename is appropriate in this case. 
            workshopName = name + "workshop" + fileNum.zfill(4)
            if self.debug: print workshopName
            workshopFilePath = os.path.join(path, workshop, workshopName)
            return workshopFilePath
            if self.debug: print workshopFilePath
        else:
            self.renameIncremental(name, folderPath)