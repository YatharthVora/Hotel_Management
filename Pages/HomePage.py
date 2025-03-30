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
if "single" not in st.session_state:
    st.session_state.single=main.getcounter("single")
if "duplex" not in st.session_state: 
    st.session_state.duplex=main.getcounter("duplex")

if "twin" not in st.session_state:
    st.session_state.twin=main.getcounter("twin")
if "suite" not in st.session_state:

    st.session_state.suite=main.getcounter("suite")
if "available" not in st.session_state:
    st.session_state.available=main.getcounter("available")
if "vacant" not in st.session_state:
    st.session_state.occupied=main.getcounter("occupied")
if "revenue" not in st.session_state:
    st.session_state.revenue=main.getcounter("revenue")


def increase(category):
    if(category=="single"):
        main.increasecounter("single")
        st.session_state.single=main.getcounter("single")
    elif category=="duplex":
        main.increasecounter("duplex")
        st.session_state.duplex=main.getcounter("duplex")
    elif category=="twin":
        main.increasecounter("twin")
        st.session_state.twin=main.getcounter("twin")
    elif category=="suite":
        main.increasecounter("suite")
        st.session_state.suite=main.getcounter("suite")
    else:
        pass
    main.increasecounter("available")
    st.session_state.available=main.getcounter("available")
    st.session_state.occupied=main.getcounter("occupied")

@st.dialog("Add Room")
def addroom():
    room_number=st.text_input("Room Number:",placeholder="Enter")
    category=st.radio("Category",["Single","Duplex","Twin","Suite"],index=None)
    if(st.button("Add")):
        increase(category.lower())
        main.add(room_number,category)
        st.rerun()


selected=option_menu(
    menu_title=None,
    options=["Home","Room","Booking","Check Out"],
    icons=["house-fill","lamp-fill","book-fill","lock-fill"],
    orientation="horizontal",
    styles=
    {
        "container": {"background-color": "#433D8B","border-radius":"0px"},
        "nav-link":#for text in the bar
        {
            "font-size": "25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected":{"background-color":"#5a0280"}
    }
)
if(selected=="Room"):
    st.switch_page("Pages/RoomPage.py")
if(selected=="Booking"):
    st.switch_page("Pages/BookingPage.py")
if(selected=="Check Out"):
    st.switch_page("Pages/CheckOut.py")


b4=st.sidebar.button("***Log out***",icon="🚪",key="logout",use_container_width=True)
if(b4):
    st.switch_page("LoginPage.py")
col1,col2=st.columns(2,border=True)
with col1:
    st.markdown("<h2 style='text-align:center;'>Category</h1>",unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    
    st.write(f"<h3>Single:{st.session_state.single}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Duplex:{st.session_state.duplex}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Twin Room:{st.session_state.twin}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Suite:{st.session_state.suite}</h3>",unsafe_allow_html=True)
        
with col2:
    st.markdown("<h2 style='text-align:center;'>Rooms</h1>",unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    st.write(f"<h3>Available:{st.session_state.available}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Occupied:{st.session_state.occupied}</h3>",unsafe_allow_html=True)
add_room=st.button("Addition of Room",key="RoomAddition",icon="➕")
if(add_room):
    addroom()
revenue_cont=st.container(border=True,key="revenue")
revenue_cont.write(f"<h1 style='margin-left:100px;'>Revenue:{st.session_state.revenue}</h1>",unsafe_allow_html=True)




if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
