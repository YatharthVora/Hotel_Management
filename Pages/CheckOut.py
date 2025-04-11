import streamlit as st
import main
import pathlib
import datetime
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("CSS file not found. Skipping custom styling.")

   
def get_booking_by_room(room_number):
    room_number = str(room_number)
    rooms = main.tracker.get_rooms()
    for room in rooms:
        if room.get("room") == room_number and room.get("status") == "occupied":
            return room
    return None

st.title("Checkout")

if st.sidebar.button("⬅️ Back", key="back_checkout"):
    st.switch_page("Pages/HomePage.py")

# Input for room number
room_number = st.text_input("Enter Room Number for Checkout")

booking_info = None
if room_number:
    booking_info = get_booking_by_room(room_number)
    if booking_info:
        st.success("Booking found for Room Number " + room_number)
    else:
        st.error("No active booking found with that room number.")

# Billing Details
st.header("Billing Details")
name = st.text_input("Full Name", value=booking_info.get("name", "") if booking_info else "")
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
    day=(datetime.datetime.strptime(booking_info['checkout'],"%d %m %y")-datetime.datetime.strptime(booking_info['checkin'],"%d %m %y")).days
    price=main.tracker.get_price(booking_info['category'],day)
    st.markdown(
        f"""
        <style>
            #category-container {{
                border: 3px solid #FF05C8;
                background-color: #202020;
                box-shadow: 0px 0px 15px 5px #FF05C8;
                font-size: 2rem;
                font-weight: 300;
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 50px;
                text-align:center;
            }}
            #inner-container {{
                display: flex;
                flex-direction: column;
                gap: 10px;
                margin-bottom:10px;
                text-align:left;
           
            }}
            #cTitle{{
             margin-top:10px;
            }}
           
        </style>

        <div id="category-container">
            <h2 style='text-align:center;' id="cTitle">Category</h2>
            <hr>
            <div id="inner-container">
                <div><b>Name: </b>{name}</div>
                <div><b>Room: </b>{booking_info['room']}</div>
                <div><b>Category: </b>{booking_info['category']}</div>
                <div><b>Check-in: </b>{booking_info['checkin']} to Check-out:{booking_info['checkout']}</div>
                <div><b>Guests: </b>{booking_info['guests']}</div>
                <div><b>Package: </b>{booking_info['package']}</div>
                <div>Total:</b>{price}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Fill in the Room Number above to view order summary.")

# Confirm and Pay
if st.button("Confirm & Pay", use_container_width=True):
    if not booking_info:
        st.error("Invalid room number or no booking info available.")
    elif not name or not email or not address or not phone:
        st.error("Please fill in all billing details.")
    elif payment_option in ["Credit Card", "Debit Card"] and (not card_number or not expiry_date or not cvv):
        st.error("Please enter valid card details.")
    elif payment_option == "UPI" and not upi_id:
        st.error("Please enter a valid UPI ID.")
    else:
        main.tracker.checkOut()
        main.tracker.checkout(room_number)
        st.success("✅ Payment Successful! Checkout confirmed.")
        
if __name__=="__main__":
     css_path=pathlib.Path("Pages/style.css")
     load_css(css_path)
