#!/usr/bin/python

# benmichae-to-the-people-of-new-york-city
# benmichae // Procedural Art Generation // Palermo To the People of New York City
# python code to procedurally generate Blink Palermo Style Images from the collection To the People of New York City.
#
# 2016-12-26 v1.1
#
# pre-reqs: PIL

#Code Notes
# based on stuff from: https://github.com/daviddoria/Examples/tree/master/Python/PIL
# and http://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

#Art Notes
#Original Inspiration is Palermo - "To the People of New York" Collection.
#Namely Coney Island II
#Each Panel is (56.8 x 52 cm), i.e. 1.092 ratio.

#Colour Notes
#4 Panels, each panel with 2 colours (top/bottom sections are always the same)
#Each colour is denoted in [R,G,B] Where R/G/B is in range from 0-255
#               s
#      |------------------|      |------------------|      |------------------|      |------------------|
#   s  |         B        |      |         D        |      |         F        |      |         H        |
#      |------------------|      |------------------|      |------------------|      |------------------|
#      |                  |      |                  |      |                  |      |                  |
#      |                  |      |                  |      |                  |      |                  |
#      |         A        |      |         C        |      |         E        |      |         G        |
#      |                  |      |                  |      |                  |      |                  |
#      |                  |      |                  |      |                  |      |                  |
#      |------------------|      |------------------|      |------------------|      |------------------|
#      |         B        |      |         D        |      |         F        |      |         H        |
#      |------------------|      |------------------|      |------------------|      |------------------|
#
#The 4 Panels is created from the following array of 8 tuples (A,B,C,D,E,F,G,H) where:
#          A               B              C               D              E                F              G                H
#  ( (32, 146, 138), (136, 58, 48), (208, 83, 51), (232, 209, 105), (27, 35, 116), (222, 142, 153), (30, 57, 52),  (212, 136, 40) )



from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

print ("benmichae-to-the-people-of-new-york-city" + str(now))
print '----------------------------------------'

#COLOUR GROUPS
#-------------

#To The People of New York City Colours Exhibition (1976)
tpnycRed    = (206,36, 49)               # red: (206,36, 49)
tpnycYellow = (249, 172, 54)          # yellow: (249, 172, 54)
tpnycBlack  = (0, 0, 0)                # black: (0, 0, 0)
#coloursToThePeopleOfNYC_I    #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_II   #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_III  #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_IV   #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_V    #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_VI   #Shape Not Yet Implemented
coloursToThePeopleOfNYC_VII   = (tpnycRed,tpnycYellow,tpnycRed,tpnycBlack,tpnycYellow,tpnycRed,tpnycBlack,tpnycRed)
coloursToThePeopleOfNYC_VIII  = (tpnycYellow,tpnycRed,tpnycYellow,tpnycBlack,tpnycRed,tpnycYellow,tpnycBlack,tpnycYellow)
coloursToThePeopleOfNYC_IX    = (tpnycRed,tpnycYellow,tpnycYellow,tpnycRed,tpnycRed,tpnycBlack,tpnycBlack,tpnycRed)
coloursToThePeopleOfNYC_X     = (tpnycYellow,tpnycRed,tpnycRed,tpnycYellow,tpnycYellow,tpnycBlack,tpnycBlack,tpnycYellow)
#coloursToThePeopleOfNYC_XI    #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_XII   #Shape Not Yet Implemented

#Coney Island II (1975)
coloursConeyIslandII = ( (32, 146, 138), (136, 58, 48), (208, 83, 51), (232, 209, 105), (27, 35, 116), (222, 142, 153), (30, 57, 52),  (212, 136, 40) )


#Times of the Day (1975)
ttdIVBrown   = (191,  86,  41)
ttdIVWhite   = (237, 241, 240)
ttdIVGrey    = (52,   52,  60)
ttdVWhite    = (237, 241, 240)
ttdVLGrey    = (210, 210, 210)
ttdVDGrey    = ( 56,  54,  59)
ttdVGreen    = (119, 198,  81)
ttdVOrange   = (194,  94,  42)
ttdVIRed     = (182,  70,  50)
ttdVIYellow  = (230,  217,  1)
ttdVIBlue    = ( 50,   80, 163)
timesOfTheDay_I      = ( (185,  55,  39), (168, 201, 216), (120, 174,  63), (167,  76,  29), (49, 123,  72), (201, 178,  76), ( 65,  33,  44),  ( 34,  33,  38) )
timesOfTheDay_II     = ( (182, 181, 179), (194, 203, 208), (218, 160,   0), (218, 216, 217), (43,  89, 148), (157, 203, 219), ( 44,  43,  49),  (160,  86,  41) )
#timesOfTheDay_III #Can't Find this artwork
timesOfTheDay_IV     = ( ttdIVWhite,ttdIVBrown,ttdIVBrown,ttdIVWhite,ttdIVBrown,ttdIVGrey,ttdIVGrey,ttdIVBrown )
timesOfTheDay_V      = ( ttdVWhite,ttdVLGrey,ttdVGreen,ttdVOrange,ttdVOrange,ttdVGreen,ttdVDGrey,ttdVLGrey )
timesOfTheDay_VI     = ( ttdVIRed,ttdVIYellow,ttdVIRed,ttdVIBlue,ttdVIBlue,ttdVIRed,ttdVIBlue,ttdVIYellow )

#Define Image Dimensions
xDimension=400 #panel width
yDimension=int(math.ceil(xDimension*1.092))  #Automatic Panel height ref correct ratio #also needs to be int, not float
smallyDimension = int(0.13*yDimension) #top and bottom colours of each panel i.e. 13% of height per stripe. no border
xSpace=100 #space around panels
ySpace=100

#Define Colour Array to Draw
colourArray = timesOfTheDay_VI    #v1.1 default option: coloursConeyIslandII

#Create Canvas
im = Image.new('RGB', (xDimension*4+xSpace*3,yDimension), (255,255,255)) #has internal spaces only
dr = ImageDraw.Draw(im)

#Create Panels in a Horizontal row (Palermo Style A)
panels=4 #number of panels
for p in range(0, panels):
    xOrigin = xDimension*p + xSpace*(p) #xOrigin=xDimension*0+xSpace*1
    dr.rectangle(((xOrigin,0),(xOrigin+xDimension,yDimension)), fill=colourArray[2*p])                          #colour= 0,2,4,6
    dr.rectangle(((xOrigin,0),(xOrigin+xDimension,smallyDimension)), fill=colourArray[2*p+1])                   #colour= 1,3,5,7
    dr.rectangle(((xOrigin,yDimension-smallyDimension),(xOrigin+xDimension,yDimension)), fill=colourArray[2*p+1])


#Complete File
#filename = "benmichae - toThePeopleOfNewYorkCity " + str(now) + " .png"
filename = "benmichae - timesOfTheDay " + str(now) + " .png"
imWithEdgeSpaces = Image.new('RGB', (xDimension*4+xSpace*5,yDimension+ySpace*2), (255,255,255)) #has internal spaces only
imWithEdgeSpaces.paste(im,(xSpace,ySpace))
imWithEdgeSpaces.save(filename) #img with spaces on each edge

print ("Wrote image to file: " + filename)
#xdg-open "rectangle.png"
