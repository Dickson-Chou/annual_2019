import cv2
import func
class dot:
    def __init__(self,pos,dia,cont):
        self.cont=cont
        self.pos=pos
        self.dia=dia
        self.bindNum=0
    def draw(self,bg):
        cv2.putText(bg,func.radiu(dia),func.Int(pos), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255), 2)

class dots:

    def __init__(self,dot,time):
        self.pos=[]
        self.dia=[]
        self.pos.append(dot.pos)
        self.dia.append(dot.dia)
        self.newPos=dot.pos
        self.newDia=dot.dia
        self.time=time
        self.times=1
        self.notFound=0
        self.Dot=1
        self.bindNum=0
    
    
    def found(self,dot):
        self.cont=dot.cont
        self.pos.append(dot.pos)
        self.dia.append(dot.dia)
        self.newPos=dot.pos
        self.newDia=dot.dia
        self.times+=1
        self.Dot+=1
        self.notFound=0
        

    def notFind(self):
        self.pos.append([])
        self.dia.append([])
        self.times+=1
        self.notFound+=1
    def draw(self,bg):
        if(self.Dot<5):
            return False
        else:
            drawdot=self.pos[-100:]
            
            for i in range(len(drawdot)-1):
                frBlo=not not drawdot[i]
                secBlo=not not drawdot[i+1]
                if(frBlo and secBlo):
                    cv2.line(bg,func.Int(drawdot[i]) , func.Int(drawdot[i+1]), (255, 0, 0), 3)
                    pass
                elif(frBlo):
                    cv2.circle(bg,func.Int(drawdot[i]), 4, (0,0, 255), -1)
                    
                    pass
                elif(secBlo):
                    cv2.circle(bg,func.Int(drawdot[i+1]), 4, (0,0, 255), -1)
                    pass
                else:
                    pass
                
    
class bind:
    def __init__(self,dot,dots,lent):
        self.dot=dot
        self.dots=dots
        self.lent=lent
