import numpy
import cv2


def MC(i,c=False):
    M = cv2.moments(i)
    mx,my=M['m10']/M['m00'],M['m01']/M['m00']
    if(c):
        return [int(mx),int(my)]
    else:
        return [mx,my]
def lent(i,j=[0,0]):
    return sum((x - y)**2 for x, y in zip(i, j))**0.5

def radiu(el):
    return numpy.sqrt(el[1][0]*el[1][1])

def Int(a):
    return (int(a[0]),int(a[1]))