#import libraries

import math as mat
import numpy as np 
import matplotlib as mpl

#set up variables

_sl, _sr = 7.25, 7.25 #distance from tracking centre to left wheel
_ss = 7.75 #distance from tracking centre to strafe wheel
_wheelradius = 3 #radius of wheels

L, R, S, = 0, 0, 0, 0 #current encoder values
θ = 0 #global orientation
pL, pR, pS, = 0, 0, 0 #previous encoder values
pθ = 0 #previous global orientationn
dL, dR, dS = 0, 0, 0 #change in encoder values (as wheel distance)
dθ = 0 #change in orientation

def getEncoderData(): #
    return eval(input("enter encoder data (L, R, S): "))
def updateEncoderData(l, r, s):
    L, R, S = l, r, s
    return None
def setEncoderDeltas():
    dL, dR, dS = ((L-pL)/360)*_wheelradius, ((R-pR)/360)*_wheelradius, ((S-pS)/360)*_wheelradius #finds distance moved from previous position
    return None
def setNewAbsoluteOrientation():
    dθ = (dL-dR)/(_sl+_sr)
    θ = pθ + dθ
    return None
    

def runTrackingAlgorithm():
    updateEncoderData(*getEncoderData()) #store the current encoder values
    setEncoderDeltas() #convert to distance travelled by the wheels and store
    setNewAbsoluteOrientation() #sets the new absolute orientation of the bot
    



while True:
    runTrackingAlgorithm()