#get news from newsapi
import streamlit as st
import datetime
import requests

st.title('Top 20 News Articles')

topic = st.selectbox('What topic are you interested in?', ('NASA space station','Rocket'), key = 'topic')
topic = topic
print(topic)
#go back 30 days from today cos this API can only fetch 30 days of data
date = datetime.date.today()-datetime.timedelta(30)

api_key = "59db1f26f881425bb636c1a71505f95c"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"from={date}&" \
      "sortBy=revelancy&" \
      f"apiKey={api_key}&" \
      "language=en"

response = requests.get(url)
#get data as json
content = response.json()
articles = content['articles'][0:20]

textbody = ""
for i,article in enumerate(articles):
      if article["title"] is not None:
            st.write(f'**{i+1}** **{article["title"]}** \n \n {article["description"]} \n \n '
                     f'Published date: {article["publishedAt"][0:10]}')
            st.write(article['url'])
