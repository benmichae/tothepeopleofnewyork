# To The People Of New York City
python code to procedurally generate Blink Palermo Style Images from the collection To the People of New York City and Times of the Day.

## To The People of New York City
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20toThePeopleOfNewYorkCity%20VII.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20toThePeopleOfNewYorkCity%20VIII.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20toThePeopleOfNewYorkCity%20IX.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20toThePeopleOfNewYorkCity%20X.png)
## Times of the Day 
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20Palermo%20-%20%20Times%20Of%20The%20Day%20I%20.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20Palermo%20-%20%20Times%20Of%20The%20Day%20II.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20Palermo%20-%20%20Times%20Of%20The%20Day%20IV.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20Palermo%20-%20%20Times%20Of%20The%20Day%20V.png)
![Screenshot](https://github.com/benmichae/tothepeopleofnewyorkcity/blob/master/benmichae%20-%20Palermo%20-%20%20Times%20Of%20The%20Day%20VI.png)

## Art Notes
* Original Inspiration is Palermo - "To the People of New York" Collection.
* Namely Coney Island II
* Each Panel is (56.8 x 52 cm), i.e. 1.092 ratio.

## Colour Notes
* 4 Panels, each panel with 2 colours (top/bottom sections are always the same)
* Each colour is denoted in R/G/B in range from 0-255
~~~~
      |------------------|      |------------------|      |------------------|      |------------------|
   s  |         B        |      |         D        |      |         F        |      |         H        |
      |------------------|      |------------------|      |------------------|      |------------------|
      |                  |      |                  |      |                  |      |                  |
      |                  |      |                  |      |                  |      |                  |
      |         A        |      |         C        |      |         E        |      |         G        |
      |                  |      |                  |      |                  |      |                  |
      |                  |      |                  |      |                  |      |                  |
      |------------------|      |------------------|      |------------------|      |------------------|
      |         B        |      |         D        |      |         F        |      |         H        |
      |------------------|      |------------------|      |------------------|      |------------------|
~~~~

The 4 Panels is created from the following array of 8 tuples (A,B,C,D,E,F,G,H) where:

~~~~
          A               B              C               D              E                F              G                H
  ( (32, 146, 138), (136, 58, 48), (208, 83, 51), (232, 209, 105), (27, 35, 116), (222, 142, 153), (30, 57, 52),  (212, 136, 40) )
~~~~
