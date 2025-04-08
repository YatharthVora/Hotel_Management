import streamlit as st
import pathlib
import pandas as pd
import main
import re
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

def filter():
    filter_dic=main.tracker.get_rooms()
    tmp=[]
    if(status_room=="All"):
        return filter_dic
    elif(status_room=="Available"):
        for i in filter_dic:
            if(i["status"]=="available"):
                tmp.append(i)
                print(tmp)
        return tmp
    elif(status_room=="Occupied"):
        for i in filter_dic:
            if(i["status"]=="occupied"):
                tmp.append(i)
                print(tmp)
        return tmp
    elif(status_room=="Name"): 
        filter_name=st.text_input("Name:",value="")
        filter_name=filter_name.lower()
        print(filter_name)
        if(filter_name!=""):
            for i in filter_dic:
                if("name" in i.keys() and i["name"]==filter_name):
                    tmp.append(i)
                    print(tmp)
            return tmp
        else:
            return filter_dic
    elif(status_room=="Category"):
        category=st.sidebar.selectbox("Category:",options=Categories)
        for i in filter_dic:
            if(i["category"]==category):
                tmp.append(i)
                print(tmp)
        return tmp
    elif(status_room=="Package"):
        package=st.sidebar.selectbox("Package:",options=packages)
        for i in filter_dic:
            if("package" in i.keys() and i["package"]==package):
                tmp.append(i)
                print(tmp)
        return tmp
    elif(status_room=="Room"):
        room=st.sidebar.multiselect("Room:",options=room_number,key="rooms")
        for j in room:
            for i in filter_dic:
                if(i["room"]==j):
                    tmp.append(i)
                    print(tmp)
        return tmp
    else:
        pass
         
rooms=main.tracker.get_rooms()
room_number=[]
room_name=[]


for i in rooms:
    for j in i:
        if(j=="room"):
            room_number.append(i[j])
        elif(j=="name"):
            room_name.append(i[j])
            pass

st.markdown("<h1 style='text-align:center;'>Rooms</h1>",unsafe_allow_html=True)

status_room=st.sidebar.selectbox("Filter",["Available","Occupied","Name","Category","Room","Package","All"],index=6)
Categories=("Single", "Duplex", "Twin","Suite")
packages=("Room Only", "Room + Resto")
rooms=list(main.tracker.get_rooms())

df=pd.DataFrame.from_dict(filter())
print(df)
st.dataframe(
    df,
    use_container_width=True,
    column_config={
        "Room":"Room",
        "Category":"Category",
        "Name":"Name",
        "Age":"Age",
        "Package":"Package",
        "Dob":"Date of Birth",
        "Check-in":"Check-in",
        "Check-out":"Check-out",
        "Guest":"Guests",
        "Status":"Status",
    },
    hide_index=True,
    on_select="ignore",
    key="table",
    )

b5=st.sidebar.button("⬅️Back",key="back_room")
if(b5):
    st.switch_page("Pages/HomePage.py")
if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
