

# Name,age,Dob,package,room number,guests,check-in,check-out,days,category
rooms={}
counter={"single":0,"duplex":0,"twin":0,"suite":0,"available":0,"occupied":0,"revenue":0}
update=False
def add(room,category):
    count=len(rooms) 
    rooms[room]={"category":category} 
    print(rooms) 
def setcounter(count,value):
    counter[count]=value
def getcounter(key):
    return counter[key]
def increasecounter(key):
    counter[key]+=1
def get_rooms():
     return rooms
def set_rooms(room,details):
    for i in details:
        rooms[room][i]=details[i]
    print(rooms)
def booked():
    counter["available"]-=1
    counter["occupied"]+=1
    update=True
def set_update():
    update=False
def update_page():
    return update





