##pip install numpy

from typing import Tuple
from numpy import set_printoptions
import pandas as pd
import numpy as np
from pandas.io import html 
import requests as re 
from requests.api import request 
from bs4 import BeautifulSoup ##web scrapper

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
    File2.write("This is line A \n")
    File2.write("This is line B \n")
    File2.write("This is line C")

with open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile2.txt","r") as readfile:
    with open("C:/Users/bruno.vallejos/Desktop/pyprog/myfile3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)

csv_path = "C:/Users/bruno.vallejos/Desktop/pyprog/myfile4.csv"

try:
    dataframe = pd.read_csv (csv_path) ## da error al querer leer y que no posea datos
except IOError:
    print("The file has no data to read")

dataframe.head()


xlsx_path = "C:/Users/bruno.vallejos/Desktop/pyprog/myfile5.xlsx"
dataframe2 = pd.read_excel (xlsx_path) ## da error al querer leer y que no posea datos. Necesita openpyxl y xlrd instalados mediante pip
dataframe2.head()

xlsx_path = "C:/Users/bruno.vallejos/Desktop/pyprog/myfile6.xlsx"
songs_frame = pd.read_excel (xlsx_path) 
songs_frame.head()
songs = {"Album":["Thriller","Back in Black","The dar side of the moon","The bodyguard","bat out of hell"], "Released":[1982,1980,1973,1992,1977],"Length":["00:42:19","00:41:11","00:42:49","00:57:44","00:46:33"]}
songs_frame = pd.DataFrame(songs)
newdf = songs_frame[["Album"]] ## me devuelve un nuevo dataframe con las columnas que yo quiera

dfunique = songs_frame["Released"].unique() 
df = songs_frame["Released"]  >= 1980 ## trae boolean 
df1 = songs_frame[df] ##colocando de nuevo dentro del dataframe, trae un dataframe filtrado

df1.to_csv("C:/Users/bruno.vallejos/Desktop/pyprog/new_songs.csv")

a = np.array([0,1,2,3,4])

print(type(a))
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.shape)

b = np.array([0.31,1.22,2,3,4])

print(type(b))
print(b.dtype)

c = np.array([20,1,2,3,4])
c[0] = 100
c[4] = 0

print(c)

d = c[1:4]

print(d)

d[1:3] = 300, 400

print (d)

##slow
u = [1,0]
v = [0,1]
z=[]

for n, m in zip(u, v):
    z.append(n + m)

##fast

u2 = np.array([1,0])
v2 = np.array([0,1])

z2 = u2 + v2

npi = np.pi

x = np.array([0, npi/2, npi])
y = np.sin(x)
print (y)

x2 = np.linspace(0, 2*np.pi, 100)
y2 = np.sin(x2)

print (y2)

a2d = [[11,12,13],
       [21,22,23],
       [31,32,33]]

a2d = np.array(a)

print (a2d.ndim)
print (a2d.shape)


url = 'https://www.ibm.com/'

r = re.get(url)
print (r.status_code)
print (r.request.body)

header = r.headers
print (header)
print (header['date'])
print (header['Content-Type'])
print (r.encoding)
print (r.text)

url_get = 'http://httpbin.org/get'
payload = {"name":"Joseph","ID":"123"}

r2 = re.get(url_get, params = payload)
print (r.url)
print (r.request.body)
print (r.text)
##print (r.json()['form'])

url_post = 'http://httpbin.org/post'
payload2 = {"name":"Joseph","ID":"123"}

r_post = re.post(url_post, data = payload2)

print ("POST request URL: ", r_post.url)
print ("GET request URL: ", r2.url)

print ("POST request body: ", r_post.request.body)
print ("GET request body: ", r2.request.body)

print (r_post.json()['form'])

paghtml = "<!DCOTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry </h3><p> Salary: $ 85,000,000 </p><h3> Kevin Durant </h3><p> Salary: $ 73,200,000 </p></body></html>"

soup = BeautifulSoup(paghtml, 'html5lib')

tag_object = soup.title
print (tag_object)
tag_object = soup.h3
print (tag_object)
tag_child = tag_object.b 
print (tag_child)
parent_tag = tag_child.parent
print (parent_tag)
sibling_1 = tag_object.next_sibling 
print (sibling_1) 
sibling_2 = sibling_1.next_sibling 
print (sibling_2) 
print (tag_child.attrs)
print (tag_child.string)


print ("End")
