from flask import Blueprint,render_template,redirect,url_for,request
from Weather_app.weather.forms import SearchForm;
import requests
from datetime import datetime
weather = Blueprint('weather',__name__)

@weather.route('/weather',methods=['GET','POST'])
def get_weather():
    url1="http://api.openweathermap.org/data/2.5/weather?units=metric&q="
    url2="http://dataservice.accuweather.com"
    appid="f2ae3da5115c395d4d31ead529c1c032" #openweathermap
    apikey="5SEC7UIIUgU156fWIhM3FkDueJ6PRf3G" #accuweather
    form = SearchForm()
    if request.method=='POST':
        if form.location.data=="":
            return render_template('weather.html',form=form)
        location=form.location.data
        r1 = requests.get(url1+location+"&appid="+appid).json() #openweathermap
        # city_key = requests.get(url2+"/locations/v1/cities/autocomplete?apikey="+apikey+"&q="+r1['name']).json()[0]['Key']
        # air = requests.get(url2+"/indices/v1/daily/1day/"+city_key+"/-10?apikey="+apikey).json()[0]['Category']
        data= {"location":r1['name'],"temp":round(r1['main']['temp']),"wind":r1['wind']["speed"],"feels":r1['main']['feels_like'],"icon":r1['weather'][0]['icon'],"disc":r1['weather'][0]['description'],"air":"Good",'time':datetime.now().strftime("%H:%M")}
        print(data)
        form.location.data = ''
        return render_template('weather1.html',form=form,data=data)
    return render_template('weather.html',form=form)
