import streamlit as st
import pathlib
import main
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

st.title("Check out")



if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)