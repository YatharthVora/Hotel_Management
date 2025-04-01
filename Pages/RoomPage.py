import streamlit as st
import pathlib
import pandas as pd
import main
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

def display():
   pass

st.markdown("<h1 style='text-align:center;'>Rooms</h1>",unsafe_allow_html=True)
Categories=("Single", "Duplex", "Twin","Suite")
packages=("Room Only", "Room + Resto")
category=st.sidebar.selectbox("Category:",options=Categories)
package=st.sidebar.selectbox("Package:",options=packages)
rooms=list(main.get_rooms())
rooms=st.sidebar.multiselect("Room:",options=rooms,key="rooms")

status_room=st.sidebar.radio("Status",["Available","Occupied","Cleaning"],index=None)
b5=st.sidebar.button("⬅️Back",key="back_room")
if(b5):
    st.switch_page("Pages/HomePage.py")
rooms=main.get_rooms()
room_number=[]
room_name=[]
room_age=[]
room_dob=[]
room_guest=[]
room_package=[]
room_check_in=[]
room_check_out=[]
room_cat=[]
room_status=[]

for i in rooms:
    for j in i:
        if(j=="room"):
            room_number.append(i[j])
        elif(j=="category"):
            room_cat.append(i[j])
        elif j=="package":
            room_package.append(i[j])
        elif(j=="name"):
            room_name.append(i[j])
        elif j=="age":
            room_age.append(i[j])
        elif j=="Dob":
            room_dob.append(i[j])
        elif j=="checkin":
            room_check_in.append(i[j])
        elif j=="checkout":
            room_check_out.append(i[j])
        elif j=="guests":
            room_guest.append(i[j])
        elif j=="status":
            room_status.append(i[j])
        else:
            pass

def filter():
    pass
df=pd.DataFrame(
    {
        "Rooms":room_number,
        "Category":room_cat,
        "Package":room_package,
        "Name":room_name,
        "Age":room_age,
        "Dob":room_dob,
        "Check-in":room_check_in,
        "Check-out":room_check_out,
        "Guest":room_guest,
        "Status":room_status,
    }    
)
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