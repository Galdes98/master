

from typing import Tuple


Name = "Bruno Vallejos"
Name2 = Name.upper()
Find = Name.find('Va')
NotFound = Name.find('asdf')
Mike = "hello Mike".find("Mike")
Tuple1 = ("hola", 1, 1.1) ## tuples are unmutable 
Tuple2 = (7, 1, 33.1)
Tuple2Sorted = sorted(Tuple2)
NestedTuple = ((1,5),("hi","bye"),99,13,(1.33,696,(1.11,11.11)))
List = ["Bruno Vallejos", 10, 1982] ##lists are mutable
List.extend([1, 1])
List.append([4, 5]) ##adds a new inside list
ListSplit = "A B C D".split()
ListSplit2 = "A,B,C,D".split(",")
List2 = List ## List2 references List and all changes
List3 = List[:] ## List3 now has a replica of List and no longer copies the values of List if it gets modified 
Dictio = {"Thriller": 1982, "Back in Black": 1980, "The Bodyguard": 1992}
Dictio['Graduation'] = 2007
Word = "Thriller"
List4 = ["Bruno","Felipe","Vallejos",1.11]
Set1 = {"hello","hi","goodbay","goodnight","goodnight"}
Set2 = set(List4)
Set2.add("NewValue")
Set2.remove("NewValue")
Set3 = {"hello","goodbay","chao"}
Set4 = Set1 & Set3
Set5 = Set1.union(Set2)

print (Name[1])
print (Name[-1])
print (Name2)
print (Find)
print (NotFound)
print (Mike)
print (Tuple1[0])
print (Tuple1[1:3])
print (len(Tuple1))
print (Tuple2Sorted)
print (NestedTuple[4][2][1])
print (List)
print (List[5]) ## brings another list
print (Dictio.keys())
print (Dictio.values())

if Word in Dictio:
    print(Word+" is inside the dictionary")
else:
    print(Word+" is not inside")

if Set4.issubset(Set1):
    print("Set 4 is inside the Set 1")
else:    
    print("Set 4 is NOT inside")

ListRange = range(10)
print (ListRange)

Squares = ["red","yellow","green","purple","blue"]
for i in range(0,5):
    Squares[i] = "white"

print (Squares)

Squares2 = ["orange","orange","purple","orange","blue"]
NewSquares = []
i = 0 

while(Squares2[i]=="orange"):
    NewSquares.append(Squares2[i])
    i = i + 1
 
def add1(a):
    b=a+1
    return b

c = add1(5)

try:
    getfile = open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile.txt","r") ## da error porque solo estoy leyendo
    ##getfile = open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile.txt","w") ## aqui si estoy escribiendo 
    ##getfile = open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile.txt","a") ## append concatena los datos
    getfile.write("My file for exception handling.")
except IOError:
    print ("Unable to open or read the data in the file.")
else:
    print ("The file was written succesfully")
finally:
    getfile.close()
    print("File is now closed.")
    
class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;

    def add_radius(self, r):
        self.radius = self.radius + r


C1 = Circle(10,"red")

C1.radius = 20
C1.color = "blue"

C1.add_radius(8) 

print(C1.radius)
print(dir(Circle))

with open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile.txt","r") as File1: ##es mejor para files porque cierra automaticamente
    file_stuff = File1.read()  ## solo funciona un read a la vez, al parecer el cursor se queda en el ultimo caracter del archivo  
    print(file_stuff)          ## y luego de hacer read() ya no encuentra nada en readlines()
    file_stuff2 = File1.readlines() 
    print(file_stuff2)
    file_stuff3 = File1.readline()
    print(file_stuff3)

##print(file_stuff)

with open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile2.txt","w") as File2:
    File2.write("This is line A")

print ("End")
