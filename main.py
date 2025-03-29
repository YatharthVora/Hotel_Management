
rooms={}
counter={"single":0,"duplex":0,"twin":0,"suite":0,"available":0,"occupied":0,"revenue":0}
def add(room,category):
    count=len(rooms) 
    rooms[room]={"category":category}  
def setcounter(count,value):
    counter[count]=value
def getcounter(key):
    return counter[key]
def increasecounter(key):
    counter[key]+=1
def getrooxm():
     pass

