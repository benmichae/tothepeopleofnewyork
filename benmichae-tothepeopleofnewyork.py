#!/usr/bin/python

# benmichae-to-the-people-of-new-york-city
# benmichae // Procedural Art Generation // Palermo To the People of New York City
# python code to procedurally generate Blink Palermo Style Images from the collection To the People of New York City.
#
# 2016-12-26
#
# pre-reqs: PIL

#Code Notes
# based on stuff from: https://github.com/daviddoria/Examples/tree/master/Python/PIL

#Art Notes
#Original Inspiration is Palermo - "To the People of New York" Collection.
#Namely Coney Island II
#Each Panel is (56.8 x 52 cm), i.e. 1.092 ratio.

#Colour Notes
#4 Panels, each panel with 2 colours (top/bottom sections are always the same)
#Each colour is denoted in [R,G,B] Where R/G/B is in range from 0-255
#
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
#The 4 Panels is created from the following array of 8 tupples (A,B,C,D,E,F,G,H) where:
#          A               B              C               D              E                F              G                H
#  ( (32, 146, 138), (136, 58, 48), (208, 83, 51), (232, 209, 105), (27, 35, 116), (222, 142, 153), (30, 57, 52),  (212, 136, 40) )



from PIL import Image, ImageFont, ImageDraw
import math

print "benmichae-to-the-people-of-new-york-city-v1"
print '-------------------------------------------'

#COLOUR GROUPS
#-------------
#Coney Island II Colours
coloursConeyIslandII = ( (32, 146, 138), (136, 58, 48), (208, 83, 51), (232, 209, 105), (27, 35, 116), (222, 142, 153), (30, 57, 52),  (212, 136, 40) )
#DEBUG print coloursConeyIslandII[1] #i.e. to get a tuple, just call it from the array


#Define Image Dimensions
xDimension=400 #panel width
yDimension=int(math.ceil(xDimension*1.092))  #Automatic Panel height ref correct ratio #also needs to be int, not float
smallyDimension = int(0.11*yDimension) #top and bottom colours of each panel i.e. 11% of height per stripe. no border
xSpace=100 #space around panels
ySpace=100

#Define Colour Array to Draw
colourArray = coloursConeyIslandII

#Create Canvas
im = Image.new('RGB', (xDimension*4+xSpace*3,yDimension), (255,255,255)) #has internal spaces only
dr = ImageDraw.Draw(im)

#Create Panels
for p in range(0, 4):
    xOrigin = xDimension*p + xSpace*(p) #xOrigin=xDimension*0+xSpace*1
    dr.rectangle(((xOrigin,0),(xOrigin+xDimension,yDimension)), fill=colourArray[2*p])                          #colour= 0,2,4,6
    dr.rectangle(((xOrigin,0),(xOrigin+xDimension,smallyDimension)), fill=colourArray[2*p+1])                   #colour= 1,3,5,7
    dr.rectangle(((xOrigin,yDimension-smallyDimension),(xOrigin+xDimension,yDimension)), fill=colourArray[2*p+1])


#Complete File
imWithEdgeSpaces = Image.new('RGB', (xDimension*4+xSpace*5,yDimension+ySpace*2), (255,255,255)) #has internal spaces only
imWithEdgeSpaces.paste(im,(xSpace,ySpace))
imWithEdgeSpaces.save("toThePeopleOfNewYorkCity.png") #img with spaces on each edge

print 'Wrote image to file: toThePeopleOfNewYorkCity.png'
#xdg-open "rectangle.png"
