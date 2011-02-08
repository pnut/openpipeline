import os

import core.file.file as file
reload(file)

class WorkshopCore(file.FileCore):
    def __init__(self, debug=1):
        self.debug = debug
        if self.debut: print 'foo WorkshopCore init'
        
    def wsCoreOpen(self, path, item, version):
        # break out workshop
        name = '%(item)s_workshop_%(version)04d.mb' % {'item': item, "version": version}     
        workshopPath = os.path.join(path, "workshop", name)
                
        if self.query(workshopPath):
            if self.debug: print workshopPath
            return workshopPath
        else:
            if self.debug: print "error"
            return
       
    
    #Returns the filename path incrementally named according to the list of files in the folder, this is specifically for workshop renaming ##pyapor##
    def wsCoreIncremental(self, name, folderPath):
        if self.debug: print 'foo'
        workshopList = self.fileCoreQueryDirList(folderPath)
        workshopLen = len(workshopList)
        workshoplen = str(workshopLen)
        if self.debug: print workshopLen + 'is the length of the workshop list'
        lastWorkshop = workshopList[len(workshopList)-1]
        if self.debug: print lastWorkshop + ' is the las workshop'
        workshopFileName = os.path.splitext(lastWorkshop)
        if self.debug: print workshopFileName
        workshopFileNumber = workshopFileName[1]
        if self.debug: print workshopFileNumber
        workshopFileNumber = int(workshopFileNumber)
        if self.debug: print workshopFileNumber
        #workshopFileNumber = workshopFileNumber + 1
        workshopFileNumber = str(workshopFileNumber)
        workshopFileName = name + "_workshop_" + workshopFileNumber.zfill(4)
        workshopPath = os.path.join(folderPath, "workshop", workshopFileName)
        if self.debug: print workshopPath
        return workshopPath
    
    #Returns the the file path of the workshop that needs to be saved. Do you prefer to return the whole path or just the renamed workshop filename? ##pyapor##
    def wsCoreSave(self, folderPath, name):
        if self.debug: print 'wsCoreSave'
        if self.fileCoreQueryDir(folderPath):
            fileNum = 1
            fileNum = str(fileNum)
            #I think that hardcoding the "workshop" into the filename is appropriate in this case. 
            workshopName = name + "workshop_" + fileNum.zfill(4)
            if self.debug: print workshopName
            workshopFilePath = os.path.join(folderPath, workshopName)
            if self.debug: print workshopFilePath
            return workshopFilePath
        else:
            self.wsCoreIncremental(name, folderPath)
            if self.debug: print workshopFilePath
            return workshopFilePath
    
    