import streamlit as st
from PIL import Image
import pathlib
from streamlit_option_menu import option_menu 
st.set_page_config(
    layout="wide"
)
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

def increase():
    pass
   
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

cat_counter=st.container()
selected=option_menu(
    menu_title=None,
    options=["Room","Booking","Check Out"],
    default_index=-1,
    icons=["lamp-fill","book-fill","lock-fill"],
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
if(selected=="Checkout"):
    pass


b4=st.sidebar.button("***Log out***",icon="🚪",use_container_width=True)

col1,col2=st.columns(2,border=True)
with col1:
    st.markdown("<h2 style='text-align:center;'>Category</h1>",unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    if(increase()):
        st.session_state.regular+=1
    st.write(f"<h3>Regular:{st.session_state.regular}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Delux:{st.session_state.delux}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>King Bed:{st.session_state.kingbed}</h3>",unsafe_allow_html=True)
        
with col2:
    st.markdown("<h2 style='text-align:center;'>Rooms</h1>",unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    if(increase()):
        st.session_state.regular+=1
    st.write(f"<h3>Available:{st.session_state.available}</h3>",unsafe_allow_html=True)
    st.write(f"<h3>Vacant:{st.session_state.vacant}</h3>",unsafe_allow_html=True)
add_room=st.button("Addition of Room",key="RoomAddition",icon="➕")
revenue_cont=st.container(border=True)
revenue_cont.write(f"<h1 style='margin-left:100px;'>Revenue:{st.session_state.revenue}</h1>",unsafe_allow_html=True)
if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
