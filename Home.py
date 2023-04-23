import streamlit as st
import pandas as pd
from Homeimage import home_image


st.set_page_config(layout = 'wide')

st.title('SpaceY Company')

home_image()

st.subheader('Our Team')

#prepare columns
col1,col2,col3 = st.columns(3)

#make dataframe with company members
df = pd.read_csv('data.csv', sep = ',')


with col1:

    for index,row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("images/" + row["image"])
        st.write(f"[Linkedin Profile]({row['url']})")

with col2:
    for index,row in df[5:9].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        #images/ is the relative path the file
        st.image("images/" + row["image"])
        #st.write("[Source Code](https://pythonhow.com)")
        st.write(f"[Linkedin Profile]({row['url']})")

with col3:
    for index,row in df[9:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("images/" + row["image"])
        st.write(f"[Linkedin Profile]({row['url']})")