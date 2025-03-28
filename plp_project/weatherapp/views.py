from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        api_key = "f9a57093cbb2ccab21957ad7cc7a5aae"

        city = request.POST['city']
        #source = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+api_key+"&units=metric").read()
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f9a57093cbb2ccab21957ad7cc7a5aae').read()
        load_data = json.loads(source)
        data = {
            "country_code": str(load_data['sys']['country']),
            "country": str(load_data['name']),
            "coordinate": str(load_data['coord']['lon']) + ':' + str(load_data['coord']['lat']),
            "cloud":str(load_data['weather'][0]['main']),
            "description": str(load_data['weather'][0]['description']),
            "humidity": str(load_data['main']['humidity']),
            "temperature": str(load_data['main']['temp_max'])+'`C',
            "pressure": str(load_data['main']['pressure']),
            'icon': load_data['weather'][0]['icon'],

                }
        #print(data)
            #return redirect(request, "index.html", {"weather":data})
    else:
        data = {}

    return render(request, "index.html", data)

