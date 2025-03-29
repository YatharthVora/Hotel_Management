import streamlit as st
import datetime
import re
import pathlib
import main
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
def main():
    
    # Room Selection
    st.sidebar.markdown("<h3 style='color:C8ACD6;'>Select Room Category</h3>",unsafe_allow_html=True)
    st.sidebar.markdown("---")
    categories = ["Single", "Duplex", "Twin","suite"]
    if "room_category" not in st.session_state:
        st.session_state.room_category = None
    for category in categories:
        if st.sidebar.button(category, key=category, use_container_width=True):
            st.session_state.room_category = None if st.session_state.room_category == category else category
    room_category = st.session_state.room_category
    if room_category:
        st.sidebar.success(f"Selected: {room_category}")
    
    # Booking Info
    st.header("Booking Information")
    name = st.text_input("Name")
    age = st.number_input("Age", 1, 120, step=1)
    dob = st.date_input("Date of Birth", value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1))
    guests = st.number_input("Number of Guests", 1, step=1)
    package = st.selectbox("Select Package", ["Room Only", "Room + Resto"])
    room_number = st.selectbox("Enter Room Number",options=["401"], placeholder="e.g., 401, 5001")
    
    # Duration of Stay (Date Range Selection)
    st.subheader("Select Stay Duration")
    today = datetime.date.today()
    check_in = st.date_input("Check-in Date", min_value=today)
    check_out = st.date_input("Check-out Date", min_value=check_in + datetime.timedelta(days=1))
    duration = (check_out - check_in).days
    
    # Booking Confirmation
    if st.button("Confirm Booking", use_container_width=True):
        try:
            if not re.match(r"^[A-Za-z ]+$", name):
                raise ValueError("Enter a valid name without numbers/special characters.")
            actual_age = datetime.date.today().year - dob.year - ((datetime.date.today().month, datetime.date.today().day) < (dob.month, dob.day))
            if actual_age != age:
                raise ValueError("Age and Date of Birth do not match.")
            if actual_age < 18:
                raise ValueError("Minimum booking age is 18.")
            if not room_category:
                raise ValueError("Select a room category.")
            if not re.match(r"^\d{1,5}$", room_number):
                raise ValueError("Enter a valid room number (e.g., 401, 5001).")
            
            st.success(f"Booking confirmed for {name} in {room_category} category.")
            st.info(f"Room Number: {room_number} | Package: {package} | Duration: {duration} nights | Guests: {guests}")
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    css_path=pathlib.Path("Pages/style.css")
    load_css(css_path)    
    main()
    if(st.sidebar.button("⬅️Back")):
        st.switch_page("Pages/HomePage.py")