import requests
import streamlit as st

def home_image():
    api = 'RcXeBVx2opmt8YOciCQO9ZQS5TP5FVYuboescMCC'
    url = f'https://api.nasa.gov/planetary/apod?api_key={api}'
    print(url)

    #to see if response successful. if successful will get a html code
    response1 = requests.get(url)

    #get data and see what is inside
    data = response1.json()
    print(data)

    #download string data as dictionary
    explanation = data['explanation']
    title = data['title']
    image_url = data['url']

    #convert string data to dictionary

    #download the image
    #print(response.content) to see code of image

    image_filepath= "image.png"
    response2=requests.get(image_url)
    with open(image_filepath, "wb") as file:
        file.write(response2.content)


    st.image(image_filepath, width=1000)
