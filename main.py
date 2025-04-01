# Name,age,Dob,package,room number,guests,check-in,check-out,days,category,status
import csv
rooms=[]
counter={"single":0,"duplex":0,"twin":0,"suite":0,"available":0,"occupied":0,"revenue":0}
# def store():
#     with open("store.csv","w") as f:
#         writer=csv.writer(f)
#         if(len(rooms)!=0):
#             for i in rooms:
#                     writer.writerow(i)
#             for i in rooms.values():
#                 writer.writerow(i)
#         for i in counter.values():
#              writer.writerow(i)

# read=[]
# def retrive():
#     with open("store.csv","r") as f:
#         csvreader=csv.reader(f)
#     print(read)





def add(room,category):
    rooms.append({"room":room,"category":category,"status:":"available"})
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
    for k,i in enumerate(rooms):
        if(i["room"]==room):
           for j in details:
               rooms[k][j]=details[j]
        print(rooms)
        break
    
def booked():
    counter["available"]-=1
    counter["occupied"]+=1






