import streamlit as st
import datetime
import re

def main():
    st.title("Booking Page")
    st.sidebar.header("Select Room Category")
    room_category = st.sidebar.radio("Category", ["Regular", "Deluxe", "King Bed"])

    categories = ["Regular", "Deluxe", "King Bed"]
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
    dob = st.date_input("Date of Birth", value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1))
    package = st.selectbox("Select Package", ["Room Only", "Room + Resto"])
    duration = st.number_input("Duration of Stay (nights)", min_value=1, step=1)

    if st.button("Confirm Booking"):
        st.success(f"Booking confirmed for {name} in {room_category} category.")
        st.info(f"Package: {package} | Duration: {duration} nights | Guests: {guests}")
    if(st.button("Home")):
        st.switch_page("Pages/HomePage.py")

=======
    
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
            st.success(f"Booking confirmed for {name} in {room_category} category.")
            st.info(f"Package: {package} | Duration: {duration} nights | Guests: {guests}")
        except ValueError as e:
            st.error(str(e))
>>>>>>> 0d6bd170ec0d40b97468b9d04b85ea5e7519fa8d

if __name__ == "__main__":
    main()    main()
