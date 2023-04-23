import requests
api_key ="d8dbddbef3471a5ce850496ee9e8eba5"

#test if url and api is correct, run this on browser
#http://api.openweathermap.org/data/2.5/forecast?q=Tokyo&appid=d8dbddbef3471a5ce850496ee9e8eba5
#for this function get place, forecast option
def get_data(place,forecast_days = None):
    #openweather.org, added in the metric to get celcius
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}"
    response = requests.get(url)
    #download content as json
    content = response.json()
    filtered_content = content['list']
    #this data set has 8 readings per day
    nr_values = 8*forecast_days
    filtered_content = filtered_content[:nr_values]
    #as the image type for the different option temp or forecast is diff, the if condition is on the main page
    return filtered_content

#runs this function only if it's in this screen
if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days=3,))
