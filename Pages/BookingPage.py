import streamlit as st
import datetime
def main():
    st.title("Booking Page")

    # Room Categories Section
    st.sidebar.header("Select Room Category")
    room_category = st.sidebar.radio("Category", ["Regular", "Deluxe", "King Bed"])

    # Booking Info Section
    st.header("Information")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    dob = st.date_input("Date of Birth", value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1))
    guests = st.number_input("Number of Guests", min_value=1, step=1)

    # Package Selection
    package = st.selectbox("Select Package", ["Room Only", "Room + Resto"])
    duration = st.number_input("Duration of Stay (nights)", min_value=1, step=1)

    if st.button("Confirm Booking"):
        st.success(f"Booking confirmed for {name} in {room_category} category.")
        st.info(f"Package: {package} | Duration: {duration} nights | Guests: {guests}")
    if(st.button("Home")):
        st.switch_page("Pages/HomePage.py")


if __name__ == "__main__":
    main()