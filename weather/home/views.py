from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        new_city = city.replace(" ","+")
        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + new_city + "&appid=569aa4697bdc9cb76feec2d87370aeef&units=metric").read()
        list_of_data = json.loads(source)
        data = {
            "country_code" : str(list_of_data["sys"]["country"]),
            "coordinates" : str(list_of_data["coord"]["lon"]) + ',' + str(list_of_data["coord"]["lat"]),
            "temp" : str(list_of_data["main"]["temp"]) + "°C",
            "pressure" : str(list_of_data["main"]["pressure"]),
            "humidity" : str(list_of_data["main"]["humidity"]),
            "main" : str(list_of_data["weather"][0]["main"]),
            "description" : str(list_of_data["weather"][0]["description"]),
            "icon" : list_of_data["weather"][0]["icon"]
        }
        print(data)
    else:
        data = {}
    return render(request,'home.html', data)

def errorpage(request):
    return render(request,'error500.html')