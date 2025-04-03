import streamlit as st
import pathlib  
import main
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
if "retrived" not in st.session_state:
    st.session_state.retrived=True
st.markdown("<h1 style='text-align:center;'>Login</h1>",unsafe_allow_html=True)
with st.form(key="login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")


if submit_button:
    if username == "admin" and password == "password":
        st.switch_page("Pages/HomePage.py")
    else:
        st.error("Invalid username or password")

if __name__=="__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)
