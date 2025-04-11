import streamlit as st
import pathlib  
import main
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
c1,c2,c3=st.columns([1,2,1])
with c2:
    st.image("logo-cropped.svg", width=800)
# st.markdown("<h1 style='text-align:center;'>Login</h1>",unsafe_allow_html=True)
with st.form(key="login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    col1, col2, col3 = st.columns([1.5,1,1])
    with col2:
        submit_button = st.form_submit_button("Login")


if submit_button:
    if username == "admin" and password == "password":
        st.switch_page("Pages/HomePage.py")
    else:
        st.error("Invalid username or password")

if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
