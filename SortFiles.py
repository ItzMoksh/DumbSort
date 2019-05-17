import re
import collections


def SortByType(fileDict):
    sorted_x = sorted(fileDict.items(), key=lambda kv: kv[1])
    FormatPrint(sorted_x)
    

def SortByName(fileDict):
    sorted_x = sorted(fileDict.items(), key=lambda kv: kv[0])
    FormatPrint(sorted_x)


def FormatPrint(sorted_x):
    sorted_dict = collections.OrderedDict(sorted_x)
    for key,value in sorted_x:
        if(value == "jpg"):
            print(key," File type: Picture")
        elif(value == "txt"):
            print(key," File type: Text")
        elif(value == "doc" or value == "pdf"):
            print(key," File type: ","Document")
        elif(value == "mp3" or value == "wav"):
            print(key," File type: ","Audio")
        else:
            print(key," File type: ","Uknown")

fileDict = {}
inputList = [ 'mallika_1.jpg', 'dog005.jpg', 'grandson_2018_01_01.png', 'dog008.jpg', 'mallika_6.jpg', 'grandson_2018_5_23.png', 'dog01.png', 'mallika_11.jpg', 'mallika2.jpg', 'grandson_2018_02_5.png', 'grandson_2019_08_23.jpg', 'dog9.jpg', 'mallika05.jpg', 'mallika08.txt','cats.txt','grandson_2018_01_01.txt', 'hello.xml','bye.txt']
for item in inputList:
    filename = item.split(".")[0]
    filename.replace("_","");
    filename = re.sub(r'[\d]','', filename)
    extension = item.split(".")[1]
    fileDict[filename] = extension

print("Sort by: \n 1) Name \n 2) Date")
opt = input()

if(opt == 1):
    SortByName(fileDict)
elif(opt == 2):
    SortByType(fileDict)

