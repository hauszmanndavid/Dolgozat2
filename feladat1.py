import random

osztaly = []

for i in range(27):
    magassag = random.randint(160, 200)
    osztaly.append(magassag)
    
print("Az osztály tanulóinak a magassága: ", osztaly)

#1 feladat 

atlag = sum(osztaly)/27
print("Az osztály tanulóinak az össz magassága: ", (sum(osztaly)))
print("Az osztály tanulóinak az átlag magassága: ", (round(atlag, 2)))

#2 feladat nem biztos hogy a legjobb
print("Ő a legmagasabb: ", max(osztaly))
print("Ő a legalacsonyabb: ", min(osztaly))
#3 feladat
print("Ennyi a magasság a legmagasabb és legalacsonyabb tanuló között cm-ben: ", max(osztaly)-min(osztaly))

#4 feladat
torony = sum(osztaly)/100
print("Össz mérték az osztályban: ", sum(osztaly))
print("Ekkora lenne a torony, ha mindenki egymás válára álna m-ben:", round(torony,2))

#5 feladat
ujtanulo = [182]
ujosztaly = osztaly + ujtanulo
print("Az új tanulóval együtt: ", ujosztaly)
#6 feladat
sorrend = ujosztaly.sort()
print("Az új tornasor: ", ujosztaly)

#7 feladat nem ment
if ():
    print("Vannak egy magasságban")
else:
    print("Nincsenek egy magasságban")