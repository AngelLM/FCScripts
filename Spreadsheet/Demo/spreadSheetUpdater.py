import doctools
import os, fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

currentPath = os.path.dirname(os.path.abspath(__file__))
freeCADfilesPaths = find('*.FCStd', currentPath)
freeCADfilePath = "C:/Users/angel.larranaga/repos/FCScripts/Spreadsheet/Demo/cilinder.FCStd"
projectXMLFolder = currentPath + "/temp"
projectXMLPath = projectXMLFolder + "/document.xml"

for freeCADfile in freeCADfilesPaths:
    if not os.path.exists(projectXMLFolder):
        os.makedirs(projectXMLFolder)

    doctools.extractDocument(freeCADfile, projectXMLFolder)
    doctools.createDocument(projectXMLPath, freeCADfile)

    for root, dirs, files in os.walk(projectXMLFolder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(projectXMLFolder)
