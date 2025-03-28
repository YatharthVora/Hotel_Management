import LoginPage
from Pages import HomePage,RoomPage,BookingPage
# Have to create a dict to store all the session state values
rooms={}
counter={}
def add(room,category):
    count=len(rooms) 
    rooms[room]={"category":category}
    print(rooms)    
    