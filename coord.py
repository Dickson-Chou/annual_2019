import numpy as np
import cv2
import math
import droplet
from func import *

red=[(160,40,40),(180,255,255)]
red2=[(0,40,40),(0,255,255)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
class cord():
    def __init__(self,img):
        self.new(img)

    def new(self,img):


        con=[[0,0],[0,1000],[1000,0],[1000,1000]]
        con=sorted(con,key=lent)
        self.cp=con
        dis=[(lent(con[0],con[1])/4.0),(lent(con[2],con[3])/4.0),
        (lent(con[0],con[2])/9.6),(lent(con[1],con[3])/9.6),
        (lent(con[0],con[3])/10.4),(lent(con[1],con[2])/10.4)]

        #CM
        self.cm=np.mean(dis)
        self.cm*=1.10118578
        #圓心
        self.mx,self.my=np.mean(con,axis=0)[0],np.mean(con,axis=0)[1]
        #目標範圍 
        self.Rang=[int(self.mx+2.45*self.cm),int(self.mx-2.45*self.cm),
        int(self.my+2.45*self.cm),int(self.my-2.45*self.cm)]
        #溢滴大小範圍
        self.dropletMax=((self.cm*0.05)**2)*math.pi*3
        self.dropletMin=((self.cm*0.05)**2)*math.pi*0.35
        print(dis)
        print(np.mean(dis))
        
        print(self.cm)


    def dropOrNot(self,i):
        c=cv2.contourArea(i)
        if(1000>c>5):
            el=cv2.fitEllipse(i)
            if(el[1][0]/el[1][1]>0.3):
                return [True,el]
        return [False,0]


    def droplan(self,a,b):

        return lent(a.pos,b.pos)

    def group(self,bindlist):

        newdot=[]
        MuiltBind=[]
        finalBind=[]

        for i in bindlist:
            if(i.dot.bindNum==1 and i.dots.bindNum==1):
                i.dots.found(i.dot)
            else:
                MuiltBind.append(i)
        sorted(MuiltBind,key=lambda s:s.lent)
        print(len(MuiltBind),end=' ')
        for i in MuiltBind:
            New=True
            for j in finalBind:
                if(i.dot is j.dot):
                    i.dot.bindNum-=1
                    New=False
                if(i.dots is j.dots):
                    i.dots.bindNum-=1
                    New=False
            if(New):
                finalBind.append(i)
        
        for i in finalBind:
            i.dots.found(i.dot)


                
            

    def binddot(self,dot,dots):
        lenLimit=self.cm*0.02
        bindList=[]
        for i in dots:
            n=0
            for k in dot:
                l=lent(i.newPos,k.pos)
                if(l<(lenLimit*(i.notFound+1))):
                    bindList.append(droplet.bind(k,i,l))
                    k.bindNum+=1
                    n+=1

            i.bindNum=n
        
        return bindList


        

#cv2.circle(img,(int(np.mean(con,axis=0)[0]),int(np.mean(con,axis=0)[1])),int(2.45*cm),(0, 255, 0),6)
