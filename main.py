# Name,age,Dob,package,room number,guests,check-in,check-out,days,category,status
import csv

class tracker:
    rooms=[]
    counter={"single":0,"duplex":0,"twin":0,"suite":0,"available":0,"occupied":0,"revenue":0}
    data=[]
    li= ["room","category","status","name","age","Dob","checkin","checkout","package","guests"]
    @classmethod
    def __init__(cls):
        cls.store_count=0
        cls.retrive()
        print("init")
    @classmethod
    def retrive(cls):
        temp={}
        with open("store.csv","r") as f:
                csvreader=csv.reader(f)
                for i in csvreader:
                        for k,v in enumerate(i):
                                temp[cls.li[k]]=v if cls.li[k]!="guests" or cls.li[k]!="age" else int(v)
                        if(len(temp)>0):
                            cls.rooms.append(temp)
                        temp={}
        print("-------------------------retrived-----------------")
        print(cls.rooms)
    @classmethod
    def add(cls,room,category):
        cls.rooms.append({"room":room,"category":category,"status":"available"})
        print(cls.rooms)
    @classmethod
    def setcounter(cls,count,value):
        cls.counter[count]=value
    @classmethod
    def getcounter(cls,key):
        return cls.counter[key]
    @classmethod
    def increasecounter(cls,key):
        cls.counter[key]+=1
    @classmethod
    def get_rooms(cls):
        return cls.rooms
    @classmethod
    def store(cls):
        with open("store.csv","w",newline="") as f:
            writer=csv.writer(f)
            for i in cls.rooms:
                    writer.writerow(list(i.values()))
        print("stored")
    @classmethod
    def set_rooms(cls,room,details):
        for k,i in enumerate(cls.rooms):
            print(i)
            if(i["room"]==room):
                for m,v in details.items():
                    cls.rooms[k][m]=v 
                break
        print(cls.rooms)
    @classmethod
    def booked(cls):
        cls.counter["available"]-=1
        cls.counter["occupied"]+=1
tracker()



            

 







    


    





