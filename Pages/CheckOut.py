import streamlit as st
import pathlib
import main
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

st.title("Check out")

if(st.sidebar.button("⬅️Back",key="back_checkout")):
    st.switch_page("Pages/HomePage.py")

if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)