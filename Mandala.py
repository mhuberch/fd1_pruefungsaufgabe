from gturtle import *

# Einen Kreis mit vorgegebenem Radius zeichnen. Ausgangsposition ist der Mittelpunkt
def kreis(radius):
    penUp()
    forward(radius)
    right(90)
    penDown()
    
    umfang = 2*3.14*radius
    repeat 720:
        forward(umfang/720)
        right(0.5)
        
    penUp()
    left(90)
    backward(radius)
    penDown()

# Einen gefuellten Kreis mit vorgegebenem Radius zeichnen. Ausgangsposition ist der Mittelpunkt
def kreis_gefuellt(radius, farbe):
    penUp()
    forward(radius)
    right(90)
    penDown()
    
    umfang = 2*3.14*radius
    setFillColor(farbe)
    startPath()
    repeat 720:
        forward(umfang/720)
        right(0.5)
    fillPath()
    
    penUp()
    left(90)
    backward(radius)
    penDown()

# Den aeusseren Kreis zeichnen
def randkreis(innenradius):
    setPenWidth(5)
    kreis(innenradius)
    setPenWidth(1)    


# Die inneren Kreise mit gewuenschter Anzahl zeichnen
def kreise_innen_gefuellt(anzahl, aussenradius):
    abstand = aussenradius/anzahl
    radius = aussenradius
    repeat anzahl:
        kreis_gefuellt(radius, "white")
        radius -= abstand


# Die Dekorationskreise ausserhalb zeichnen
def dekokreise(grosser_radius, durchmesser, anzahl):
    winkel = 360/anzahl
    # Die Dekokreise sind versetzt zu den Blaettern um genau die Haelfte
    # des Winkels zwischen den Blaettern
    left(winkel/2)
    repeat anzahl:
        penUp()
        # Von der Mitte bis kurz vor dem Aussenkreis bewegen
        forward(grosser_radius - durchmesser/2 - 8)
        penDown()
        
        kreis(durchmesser/2)
        # Nach dem Zeichnen des Kreises wieder zurueck zum Mittelpunkt
        # gelangen, ohne Spuren zu hinterlassen
        penUp()
        backward(grosser_radius - durchmesser/2 - 8)
        penDown()      
        # Vom Mittelpunkt aus um einen Schritt nach rechts drehen
        # um in Richtung des naechsten Dekokreises zu schauen
        right(winkel)
        

# Ein einzelnes Blatt bestehend aus zwei Drittelkreisen zeichnen
def blatt(durchmesser):
    radius_blatt = 2*durchmesser/sqrt(3)
    winkel = 120
    left(120)
    repeat 2:
        right(60)
        blatt_haelfte(winkel, radius_blatt/2)
    right(120)

# Ein einzelnes Blatt bestehend aus zwei Drittelkreisen zeichnen ausgefuellt mit Farbe
def blatt_gefuellt(durchmesser, farbe):
    radius_blatt = 2*durchmesser/sqrt(3)
    winkel = 120
    left(120)
    setFillColor(farbe)
    startPath()
    repeat 2:
        right(60)
        blatt_haelfte(winkel, radius_blatt/2)
    fillPath()
    right(120)

# Das Blatt, das in blatt(...), blatt_gefuellt(...) gezeichnet wird, besteht aus zwei derartigen Haelften
def blatt_haelfte(winkel, radius):
    umfang = 2*3.14*radius
    bogenlaenge = umfang/360*winkel
    repeat winkel:
        forward(bogenlaenge/winkel)
        right(1)

# Die Blumenblaetter zeichnen lassen
def blumenblaetter(durchmesser, anzahl):
    winkel = 360/anzahl
    repeat anzahl:
        blatt(durchmesser)
        right(winkel)
    
        
makeTurtle()
hideTurtle()

gesamtradius = 200
anzahl_innenkreise = 5
anzahl_blaetter = 8

# Zeichnet aeussere Kreise als Rand
randkreis(gesamtradius)

# die Blumenblaetter des Mandalas
blumenblaetter(gesamtradius, anzahl_blaetter)

# die inneren Kreise: die Anzahl ist veraenderlich
kreise_innen_gefuellt(anzahl_innenkreise, gesamtradius/2)

# die kleinen Kreise am aeusseren Rand
dekokreise(gesamtradius, 10, anzahl_blaetter)

    