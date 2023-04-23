import requests
api_key ="d8dbddbef3471a5ce850496ee9e8eba5"

#test if url and api is correct, run this on browser
#http://api.openweathermap.org/data/2.5/forecast?q=Tokyo&appid=d8dbddbef3471a5ce850496ee9e8eba5
#for this function get place, forecast option
def get_data(place,forecast_days = None):
    #openweather.org
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    #download content as json
    content = response.json()
    filtered_content = content['list']
    nr_values = 8*forecast_days
    filtered_content = filtered_content[:nr_values]
    #as the image type for the different option temp or sky is diff, the if condition is on the main page
    return filtered_content

#runs this function only if it's in this screen
if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days=3,))
    # dates = ["2022-25-10","2022-26-10","2022-27-10"]
    # temperatures = [34,25,36]
    # temperatures = [days * i for i in temperatures]
    # # return dates, temperatures