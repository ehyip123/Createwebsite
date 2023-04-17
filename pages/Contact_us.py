import streamlit as st
from send_email import send_email

#text in bracket would be the page name
#each py file under the pages would be a page on the website shown on the sidebar
st.write('Leave your Message')

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    enquiry_type = st.selectbox('What is the nature of your enquiry', ('Business Proposal', 'Networking', 'Others'))

    raw_message = st.text_area("Type your message here")

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Enquiry type: {enquiry_type}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")