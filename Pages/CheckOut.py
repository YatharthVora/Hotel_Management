import streamlit as st
import pathlib
import pandas as pd
import main

CSV_FILE = "store.csv"

def fetch_booking_details(room_number):
    try:
        df = pd.read_csv(CSV_FILE, header=None)  # No headers in CSV
        df.columns = ["Room Number", "Room Category", "Status", "Name", "Age", "DOB", 
                      "Check-in", "Check-out", "Package", "Guests"]
        
        df["Room Number"] = df["Room Number"].astype(str)  # Ensure room number is string
        
        booking = df[df["Room Number"] == str(room_number)]  # Search for room number

        if booking.empty:
            return None  # No matching room found
        
        return booking.iloc[0].to_dict()  # Convert first match to dictionary

    except FileNotFoundError:
        st.error(f"Error: '{CSV_FILE}' not found. Make sure the file exists.")
        return None

def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("CSS file not found. Skipping custom styling.")

st.title("Checkout")

if st.sidebar.button("⬅️ Back", key="back_checkout"):
    st.switch_page("Pages/HomePage.py")

# Fetch Room Number from Session State
room_number = st.session_state.get("room_number")

# Fetch Booking Details
booking_info = fetch_booking_details(room_number) if room_number else None

# Billing Information
st.header("Billing Details")
name = st.text_input("Full Name", value=booking_info["Name"] if booking_info else "")
email = st.text_input("Email")
address = st.text_area("Billing Address")
phone = st.text_input("Phone Number")

# Payment Method
st.header("Payment Method")
payment_option = st.radio("Select Payment Method", ["Credit Card", "Debit Card", "UPI", "Net Banking"], horizontal=True)

if payment_option in ["Credit Card", "Debit Card"]:
    card_number = st.text_input("Card Number")
    expiry_date = st.text_input("Expiry Date (MM/YY)")
    cvv = st.text_input("CVV", type="password")
elif payment_option == "UPI":
    upi_id = st.text_input("Enter UPI ID")

# Order Summary
st.header("Order Summary")
if booking_info:
    st.text(f"Room Category: {booking_info['Room Category']}")
    st.text(f"Duration: {booking_info['Check-in']} to {booking_info['Check-out']}")
    st.text(f"Total Guests: {booking_info['Guests']}")
    total_price = st.session_state.get("total_price", "N/A")
    st.text(f"Total Price: ${total_price}")
else:
    st.error("No booking found. Please check your booking details.")

# Confirm and Pay Button
if st.button("Confirm & Pay", use_container_width=True):
    if not name or not email or not address or not phone:
        st.error("Please fill in all billing details.")
    elif payment_option in ["Credit Card", "Debit Card"] and (not card_number or not expiry_date or not cvv):
        st.error("Please enter valid card details.")
    elif payment_option == "UPI" and not upi_id:
        st.error("Please enter a valid UPI ID.")
    else:
        st.success("Payment Successful! Your booking is confirmed.")

if __name__ == "__main__":
    css_path = pathlib.Path("Pages/style.css")
    load_css(css_path)
