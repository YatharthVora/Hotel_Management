import streamlit as st
import pathlib
from streamlit_extras.dataframe_explorer import dataframe_explorer
st.set_page_config(
    layout="wide"
)
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

def display():
   pass

st.markdown("<h1 style='text-align:center;'>Rooms</h1>",unsafe_allow_html=True)
Categories=("Regular", "Deluxe", "King Bed")
packages=("Room Only", "Room + Resto")
category=st.sidebar.multiselect("Category:",options=Categories)
package=st.sidebar.multiselect("Package:",options=packages)
rooms=["101","102","103"]
rooms=st.sidebar.multiselect("Room:",options=rooms)

status_room=st.sidebar.radio("Status",["Available","Occupied","Cleaning"],index=None)

if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)