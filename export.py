import os
import droplet
import numpy as np
import csv
import shutil
import zipfile
import cv2
cache = ".\\csvcache"


if os.path.isdir(cache):
    shutil.rmtree(cache)

os.mkdir(cache)
cache += '\\'

def Achive_Folder_To_ZIP(sFilePath,f):
  
    zf = zipfile.ZipFile(f + '.ZIP', mode='w')#只儲存不壓縮
    #zf = zipfile.ZipFile(sFilePath + '.ZIP', mode = 'w', compression = zipfile.ZIP_DEFLATED)#預設的壓縮模式
    os.chdir(sFilePath)
    #print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            #print aFile
            zf.write(aFile)
    zf.close()
def csvD(Dots,file,co):
    with open(cache+'main.csv', 'w', newline='') as csvfile:
    
        maincsv = csv.writer(csvfile)

        maincsv.writerow([file])
        maincsv.writerow([len(Dots),co[0],co[1],co[2]])
      
        
        for i in Dots:
            x=np.mean(arr(i.pos), axis=0)[0]
            y=np.mean(arr(i.pos), axis=0)[1]
            pol=cv2.cartToPolar(x-int(co[1])-0.5,y-int(co[1])-0.5,angleInDegrees=True)
            name=str(pol[1][0][0])+'_'+str(pol[0][0][0])
            maincsv.writerow([])
            print(arr(i.dia))
            maincsv.writerow([name,np.mean(arr(i.dia)),pol[0][0][0],pol[1][0][0],(i.times-i.Dot-1)])

            with open(cache+str(name)+'.csv', 'w', newline='') as csvD:
                dotcsv = csv.writer(csvD)
                dotcsv.writerow([i.time])
                dotcsv.writerows(i.pos[2:])
    Achive_Folder_To_ZIP(cache,file)
    
def arr(lists):
    final=[]
    for i in lists:
        if (not not i):
            final.append(i)
    return np.array(final)

