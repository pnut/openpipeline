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
        workshopList = self.fileCoreQueryDirList(folderPath)
        if self.debug: print "List of workshop files:"
        if self.debug: print workshopList
        workshopLen = len(workshopList)
        workshopLen = str(workshopLen)
        if self.debug: print 'There are ' + workshopLen + ' workshop files in' + folderPath + '.'
        lastWorkshop = workshopList[len(workshopList)-1]
        if self.debug: print lastWorkshop + ' is the last workshop.'
        workshopFileName = os.path.splitext(lastWorkshop)
        if self.debug: print workshopFileName[0] + ' is the name of the last workshop file.' 
        workshopFileName = workshopFileName[0]
        
        workshopFileNumber = workshopFileName[-4:]
        if self.debug: print workshopFileNumber + ' is number of the last workshop.'
        workshopFileNumber = int(workshopFileNumber)
        workshopFileNumber += 1
        workshopFileNumber = str(workshopFileNumber)
        if self.debug: print workshopFileNumber + ' is number of the new workshop.'
        
        workshopFileName = name + "_workshop_" + workshopFileNumber.zfill(4)
        workshopPath = os.path.join(folderPath, workshopFileName)
        if self.debug: print workshopPath
        return workshopPath
    
    #Returns the the file path of the workshop that needs to be saved. Do you prefer to return the whole path or just the renamed workshop filename? ##pyapor##
    def wsCoreSave(self, folderPath, name):
        if self.debug: print 'wsCoreSave'
        if self.fileCoreQueryDir(folderPath):
            fileNum = 1
            fileNum = str(fileNum)
            #I think that hardcoding the "workshop" into the filename is appropriate in this case. ##pyapor## 
            workshopName = name + "_workshop_" + fileNum.zfill(4)
            if self.debug: print workshopName + ' is the workshop file name.'
            workshopFilePath = os.path.join(folderPath, workshopName)
            if self.debug: print workshopFilePath
            return workshopFilePath
        else:
            workshopFilePath = self.wsCoreIncremental(name, folderPath)
            if self.debug: print workshopFilePath
            return workshopFilePath
    
    