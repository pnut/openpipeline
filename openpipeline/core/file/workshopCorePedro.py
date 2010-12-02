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
       
    
    #Returns the filename path incrementally named according to the list of files in the folder, this is specifically for workshop renaming ##pyapor##
    def wsCoreIncremental(self, name, folderPath):
        workshopList = self.fileCoreQueryDirList(folderPath)
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
    def wsCoreSave(self, name, folderPath):
        if self.fileCoreQueryDir(folderPath):
            fileNum = 1
            #I think that hardcoding the "workshop" into the filename is appropriate in this case. 
            workshopName = name + "workshop" + fileNum.zfill(4)
            if self.debug: print workshopName
            workshopFileName = os.path.join(path, workshop, workshopName)
            if self.debug: print workshopFileName
        else:
            self.renameIncremental(name, folderPath)
    