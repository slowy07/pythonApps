import datetime
import os
import shutil

timeToday = datetime.datetime.today()
setStringDate = timeToday.isoformat()


configDir = os.getenv("my_config")
dropbox = os.getenv("dropbox")
configFile = 'services.conf'
cofigFilename = os.path.join(configDir, configFile)
sourceDir = os.path.expanduser('~/Library/Services/')
destinationDir = os.path.join(dropbox, "myBackups"+"/"+"AutomaterServices"+setStringDate+"/")

for detFilename in open(cofigFilename):
    fileName = detFilename.strip()
    if fileName:
        sourceFile = os.path.join(sourceDir, fileName)
        destFilename = os.path.join(destinationDir, fileName)
        shutil.copytree(sourceFile, destFilename)
