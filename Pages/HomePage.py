import streamlit as st
import pathlib
from streamlit_option_menu import option_menu 
import main
import atexit
st.set_page_config(
    layout="wide"
)
class error(Exception):
    pass
class InvalidRoomInput(error):
    pass
class InputCategory(error):
    pass
class Exists(error):
    pass
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
if(main.tracker.Book):
    print("checkout")
    st.session_state.available=main.tracker.getcounter("available")
    st.session_state.revenue=main.tracker.getcounter("revenue")
    main.tracker.Book=False

if "single" not in st.session_state:
    st.session_state.single=main.tracker.getcounter("single")
if "duplex" not in st.session_state: 
    st.session_state.duplex=main.tracker.getcounter("duplex")
if "twin" not in st.session_state:
    st.session_state.twin=main.tracker.getcounter("twin")
if "suite" not in st.session_state:

    st.session_state.suite=main.tracker.getcounter("suite")
if "available" not in st.session_state:
    st.session_state.available=main.tracker.getcounter("available")
if "vacant" not in st.session_state:
    st.session_state.occupied=main.tracker.getcounter("occupied")
if "revenue" not in st.session_state:
    st.session_state.revenue=main.tracker.getcounter("revenue")
if "total" not in st.session_state:
    st.session_state.total=main.tracker.getcounter("available")
def increase(category):
    if(category=="single"):
        main.tracker.increasecounter("single")
        st.session_state.single+=1
    elif category=="duplex":
        main.tracker.increasecounter("duplex")
        st.session_state.duplex=main.tracker.getcounter("duplex")
    elif category=="twin":
        main.tracker.increasecounter("twin")
        st.session_state.twin=main.tracker.getcounter("twin")
    elif category=="suite":
        main.tracker.increasecounter("suite")
        st.session_state.suite=main.tracker.getcounter("suite")
    else:
        pass
    main.tracker.increasecounter("available")
    st.session_state.available=main.tracker.getcounter("available")
    st.session_state.occupied=main.tracker.getcounter("occupied")

@st.dialog("Add Room")
def addroom():
    try:
        room_number=st.text_input("Room Number:",placeholder="Enter")
        category=st.radio("Category",["Single","Duplex","Twin","Suite"],index=None)
        if(st.button("Add")):
            if(room_number==""):
                raise InvalidRoomInput
            if(category==None):
                raise InputCategory
            li=main.tracker.get_rooms()
            for i in li:
                for j in i.values():
                    if(j==room_number):
                        raise Exists
            increase(category.lower())
            main.tracker.add(room_number,category)
            st.session_state.total=st.session_state.available+st.session_state.occupied
            st.rerun()
    except InvalidRoomInput:
        st.error("Enter the room")
    except InputCategory:
        st.error("Select the Category")
    except Exists:
        st.error("Exists")
   

selected=option_menu(
    menu_title=None,
    options=["Home","Room","Booking","Check Out"],
    icons=["house-fill","lamp-fill","book-fill","lock-fill"],
    orientation="horizontal",
    styles=
    {
        "container": {"background-color": "#8701ac","border-radius":"0px"},
        "nav-link":#for text in the bar
        {
            "font-size": "25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#D06AEC",
        },
        "nav-link-selected":{"background-color":"#AE02DD"}
    }
)
dic=main.tracker.get_counter()
stats={}
for i in dic:
    if( i not in ["available","occupied","revenue"]):
        stats[i]=st.session_state[i]

st.bar_chart(stats,horizontal=True,height=250,color="#FF05C8")
room_category=st.container()
with room_category:
    st.markdown(
        f"""
        <style>
            #category-container {{
                border: 3px solid #FF05C8;
                background-color: #202020;
                color: white;
                box-shadow: 0px 0px 15px 5px #FF05C8;
                font-size: 2rem;
                font-weight: 300;
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 50px;
            }}
            #inner-container {{
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
                gap: 10px;
                margin-bottom:10px;
           
            }}
            #cTitle{{
             margin-top:10px;
            }}
           
        </style>

        <div id="category-container">
            <h2 style='text-align:center;' id="cTitle">Category</h2>
            <hr>
            <div id="inner-container">
                <div><h3>Single: {st.session_state.single}</h3></div>
                <div><h3>Duplex: {st.session_state.duplex}</h3></div>
                <div><h3>Twin Room: {st.session_state.twin}</h3></div>
                <div><h3>Suite: {st.session_state.suite}</h3></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.bar_chart({"Available":dic["available"],"Occupied":dic["occupied"],"Total":st.session_state.total},horizontal=True,height=250,color=["#00FFF5"])
    room_type=st.container()
    with room_type:
            st.markdown(
        f"""
         <style>
            #room-container {{
                 border: 3px solid #00FFF5;
            background-color: #202020;
            color: white;
            box-shadow: 0px 0px 15px 5px #00FFF5;
            font-size: 2rem;
            font-weight: 300;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 50px;
            }}
            #inner-container2 {{
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
                gap: 10px;
                margin-bottom:10px;
           
            }}
            #inner-container2 div:nth-child(1){{
                margin-left:50px;
            }}
            #inner-container2 div:nth-child(2){{
                margin-right:70px;
            }}
       </style>
        <div id="room-container">
            <h2 style='text-align:center;' id="cTitle">Rooms</h2>
            <hr>
            <div id="inner-container2">
                <div><h3>Available:{st.session_state.available}</h3></div>
                <div><h3>Occupied:{st.session_state.occupied}</h3></div>
                <div><h3>Total:{st.session_state.total}</h3></div>
            </div>
        """,
        unsafe_allow_html=True
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




add_room=st.button("Addition of Room",key="RoomAddition",icon="➕")
if(add_room):
    addroom()

st.bar_chart({"Target":st.session_state.revenue*2 if st.session_state.revenue!=0 else 10000,"Achieved":st.session_state.revenue},horizontal=True,height=250,color="#FFE605")
revenue_cont=st.container()
with revenue_cont:
    st.markdown(
        f"""
         <style>
            #revenue-container {{
                 border: 3px solid #FFE605;
            background-color: #202020;
            color: white;
            box-shadow: 0px 0px 15px 5px #FFE605;
            font-size: 2rem;
            font-weight: 300;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 50px;
            }}
            #inner-container3 {{
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
                gap: 10px;
                margin-bottom:10px;
           
            }}
            #inner-container3 div:nth-child(1){{
                margin-left:50px;
            }}
       </style>
        <div id="revenue-container">
            <h2 style='text-align:center;' id="cTitle">Revenue:{st.session_state.revenue}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    

atexit.register(main.tracker.store)

if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)


