"""#importing libraries

import math as mat
import numpy as np
import matplotlib as mpl

#setting up variables

pi=np.pi

sl = 7.25 #distance from tracking centre to left wheel
sr = 7.25 #distance from tracking centre to right wheel

x, y, r = 0.0, 0.0, 0.0 #initial position
xd = 0 #change in x this iteration
yd = 0 #change in y this iteration
rd = 0 #change in rotation this iteration (radians)
encoderdata = (0, 0) #stores encoder data from current cycle
prevencoderdata = (0, 0) #stores encoder data from previous cycle

#setting up functions

def getEncoderData(): #gets current encoder data
    return eval(input("input encoder data (l, r): ")) #placeholder input to be replaced by encoder data

def getAngleTurned(L, R): #gets angle turned as compared to previous loop cycle
    return (L - R) / (sl +sr) #output in radians

def getLocalTranslation(L, R, θ): #gets how far the robot has moved alonng the X and Y axes compared to its previous position
    if θ == 0:
        return (0, (L + R) / 2)  #straight movement
    else:
        y = 2 * mat.sin(θ / 2) * ((R / θ) + sr)
        return (0, y)

#main loop

while True: 
    encoderdata= getEncoderData()
    rd=getAngleTurned(*encoderdata)
    print("angle turned (deg):", mat.degrees(rd))
    xd, yd = getLocalTranslation(*encoderdata, rd)
    print("local Y displacement:", yd)"""