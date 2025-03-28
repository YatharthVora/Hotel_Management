import LoginPage
from Pages import HomePage,RoomPage,BookingPage

rooms={}
count =0
def add(room,category):
    count=len(rooms) 
    if(count==0):
        count+=1
    rooms[room]={"category":category}
    print(rooms)
    