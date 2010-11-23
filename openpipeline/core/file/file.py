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
    
    #get the file name.
    def fileCoreFileName(self):
        fileName = os.path.split(self.filePath)
        if self.debug: print 'the fileName : ' + fileName[1]
        
    #get the path without the file name.
    def fileMayaLoc (self):
        mayaLoc = os.path.split(self.filePath)
        locDir = mayaLoc[0]
        if self.debug: print 'the locDir : ' + locDir
        return locDir
    
    #make a folder.
    def fileCoreMakeFolder(self, folderName):
        folderPath = os.path.join(self.filePath, folderName)

	if self.query(folderPath):
            if self.debug: print 'the folder' + folderName + 'is already exist.'
            pass
	else:
            os.mkdir(self.filePath + "/" + folderName)
	    if self.debug: print 'the folder' + folderName + ' has been created under : ' + folderPath
            
    #make three folders automatically.
    def fileCoreMakeProjFolder(self, projectFolder):
        self.projFolderName = projectFolder
	projFolderPath = os.path.join(self.filePath, self.projFolderName)
	print "projFolderPath : " +  projFolderPath

	if self.query(projFolderPath):
		if self.debug: print 'the folder ' + projFolderName + 'is already exist.'
		pass
	else:
	
		os.mkdir(self.filePath + "/" + projFolderName)
		os.mkdir(projFolderPath + "/workshopFiles")
		os.mkdir(projFolderPath + "/masterFiles")
		if self.debug: print 'the project folder ' + projFolderName + ' has been created under : ' + projFolderPath
				    


