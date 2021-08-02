import requests
from tkinter import Tk, Label, Entry, Frame, Button

degree_sign = u"\N{DEGREE SIGN}"

class WeatherAPP():
    # * api key for connect the web server
    __weather_api_key = "User API KEY"
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title('Weather App')

        # * Search Bar
        searchbar = Label(self.root)
        searchbar.pack(fill='both')

        Label(searchbar, text='Enter City Name').pack(fill='x',expand=True,side='left')

        self.entry_box = Entry(searchbar)
        self.entry_box.pack(fill='x',expand=True,side='left')
        
        Button(searchbar,text='Search',command=self.search).pack(fill='x',expand=True)

        # * Result Panel
        result_panel = Frame(self.root)
        result_panel.pack(fill='both',expand=True)

        self.l_weather = Label(result_panel)
        self.l_weather.pack(fill='both',expand=True)

        self.l_temp = Label(result_panel)
        self.l_temp.pack(fill='both',expand=True)
        
        self.l_humidity = Label(result_panel)
        self.l_humidity.pack(fill='both',expand=True)
        
        self.l_wind = Label(result_panel)
        self.l_wind.pack(fill='both',expand=True)

        # * MainLoop
        self.root.mainloop()
    
    def search(self):
        self.l_weather.config(text='')
        self.l_temp.config(text='')
        self.l_humidity.config(text='')
        self.l_wind.config(text='')
        
        city_name = self.entry_box.get()
        # * url to fetch
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city_name,self.__weather_api_key)
        res = requests.get(url)
        self.print_to_screen(res.json())

    def print_to_screen(self,output):
        try:
            weather_text = 'Weather: {}'.format(output['weather'][0]['description'])
            # splited because it is very lengthy
            temp_text = 'Temperature: {} {}C \n Feels Like: {} {}C'.format(output['main']['temp'],degree_sign,
                                                                           output['main']['feels_like'],degree_sign)
            temp_text = temp_text + '\n Min temp: {} {}C \n Max temp: {} {}C'.format(output['main']['temp_min'],degree_sign,
                                                                                     output['main']['temp_max'],degree_sign)

            humidity_text = 'Humidity: {}'.format(output['main']['humidity'])
            wind_text = 'Wind Speed: {}'.format(output['wind']['speed'])

            self.l_weather.config(text=weather_text,fg='#000000')
            self.l_temp.config(text=temp_text)
            self.l_humidity.config(text=humidity_text)
            self.l_wind.config(text=wind_text)
        except Exception:
            self.l_weather.config(text=output['cod'] + " : " + output['message'],fg="#ff0000")


# * App runs
if __name__ == "__main__":
    WeatherAPP()