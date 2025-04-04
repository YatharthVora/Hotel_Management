import streamlit as st
import pathlib
import pandas as pd
import main

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

def filter():
    fliter_dic=main.tracker.get_rooms()
    tmp=[]
    if(status_room=="All"):
        return fliter_dic
    elif(status_room=="Available"):
        for i in fliter_dic:
            if(i["status"]=="available"):
                tmp.append(i)
                print(tmp)
        return tmp
    elif(status_room=="Occupied"):
        for i in fliter_dic:
            if(i["status"]=="occupied"):
                tmp.append(i)
                print(tmp)
        return tmp
         
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
Categories=("Single", "Duplex", "Twin","Suite")
packages=("Room Only", "Room + Resto")
category=st.sidebar.selectbox("Category:",options=Categories)
package=st.sidebar.selectbox("Package:",options=packages)
rooms=list(main.tracker.get_rooms())
rooms=st.sidebar.multiselect("Room:",options=room_number,key="rooms")
filter_name=st.text_input("Name:")
status_room=st.sidebar.radio("Status",["Available","Occupied","All"],index=2)
b5=st.sidebar.button("⬅️Back",key="back_room")
if(b5):
    st.switch_page("Pages/HomePage.py")


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


if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
