import streamlit as st
import pathlib
from streamlit_option_menu import option_menu 
import main
st.set_page_config(
    layout="wide"
)
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
if "regular" not in st.session_state:
    st.session_state.regular=0 
if "delux" not in st.session_state: 
    st.session_state.delux=0

if "kingbed" not in st.session_state:
    st.session_state.kingbed=0
if "available" not in st.session_state:
    st.session_state.available=0
if "vacant" not in st.session_state:
    st.session_state.vacant=0
if "revenue" not in st.session_state:
    st.session_state.revenue=0

def increase(category):
    if(category=="Regular"):
        st.session_state.regular+=1
    elif category=="Deluxe":
        st.session_state.delux+=1
    elif category=="King bed":
        st.session_state.kingbed+=1
    else:
        pass
    st.session_state.available+=1

@st.dialog("Add Room")
def addroom():
    room_number=st.text_input("Room Number:",placeholder="Enter")
    category=st.radio("Category",["Regular","Deluxe","King bed"],index=None)
    if(st.button("Add")):
        increase(category)
        main.add(room_number,category)
        st.rerun()



selected=option_menu(
    menu_title=None,
    options=["Home","Room","Booking","Check Out"],
    icons=["house-fill","lamp-fill","book-fill","lock-fill"],
    orientation="horizontal",
    styles=
    {
        "container": {"background-color": "#D7C0AE","border-radius":"0px"},
        "nav-link":#for text in the bar
        {
            "font-size": "25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
    }
)
if(selected=="Room"):
    st.switch_page("Pages/RoomPage.py")
if(selected=="Booking"):
    st.switch_page("Pages/BookingPage.py")
if(selected=="Check Out"):
    st.switch_page("Pages/CheckOut.py")


b4=st.sidebar.button("***Log out***",icon="🚪",key="logout",use_container_width=True)

col1,col2=st.columns(2,border=True)
with col1:
    st.markdown("<h2 style='text-align:center;'>Category</h1>",unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    
    st.write(f"<h3>Regular:{st.session_state.regular}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Delux:{st.session_state.delux}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>King Bed:{st.session_state.kingbed}</h3>",unsafe_allow_html=True)
        
with col2:
    st.markdown("<h2 style='text-align:center;'>Rooms</h1>",unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    st.write(f"<h3>Available:{st.session_state.available}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Vacant:{st.session_state.vacant}</h3>",unsafe_allow_html=True)
add_room=st.button("Addition of Room",key="RoomAddition",icon="➕")
if(add_room):
    addroom()
revenue_cont=st.container(border=True,key="revenue")
revenue_cont.write(f"<h1 style='margin-left:100px;'>Revenue:{st.session_state.revenue}</h1>",unsafe_allow_html=True)
if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
