import requests
from tkinter import *

def search_city(event):
    city = e1.get()
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=672a7cc8e25afb516dc96857806c7d0e")
    data = response.json()
    listbox.delete(0, END)
    for item in data:
        listbox.insert(END, item['name'])

def get_weather(event):
    city = listbox.get(ANCHOR)
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=672a7cc8e25afb516dc96857806c7d0e")
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15
        result.set(f"Weather: {weather}, Temperature: {temp_c:.2f}°C")
    else:
        result.set("Unable to get weather data.")

master = Tk()
Label(master, text="City:").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
e1.bind('<KeyRelease>', search_city)
listbox = Listbox(master)
listbox.grid(row=1, column=1)
listbox.bind('<<ListboxSelect>>', get_weather)
result = StringVar()
Label(master, textvariable=result).grid(row=2, columnspan=2)
mainloop()