import streamlit as st
import pathlib  
st.set_page_config(
    layout="wide"
)
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

st.title("Login")
if(st.button("Next")):
    st.switch_page("Pages/HomePage.py")
    
if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
