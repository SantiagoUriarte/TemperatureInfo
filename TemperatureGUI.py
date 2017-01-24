from tkinter import *
import urllib.request
import json

key = "dd29faab298c99921ec95069c3b99bfe"


def setUnitI(event):
    dUnits.set("degrees Fahrenheit")
    hidden.delete(0, END)
    hidden.insert(1, "imperial")

def setUnitM(event):
    dUnits.set("degrees Celsius")
    hidden.delete(0, END)
    hidden.insert(1, "metric")

def getInfo(zipc, area, unit):
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipc + "," + area + "&appid=" + key + "&units=" + unit
    obj = urllib.request.urlopen(str(url))
    data = str(obj.read())
    data = data[2:(len(data) - 1)]
    jData = json.loads(data)
    return jData

def getCountry(jData):
    countryKey = jData['sys']
    return countryKey['country']

def getName(jData):
    return jData['name']

def getTemp(jData):
    tempKey = jData['main']
    return(tempKey['temp'])

def reset(event):
    dTemp.delete(0, END)
    dName.delete(0, END)
    zipE.delete(0, END)
    countryE.delete(0, END)
    hidden.delete(0, END)
    dUnits.set("")


def getURL(event):
    urlTest.delete(0, END)
    zipc = zipE.get()
    area = countryE.get()
    unit = hidden.get()
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipc + "," + area + "&appid=" + key + "&units=" + unit
    urlTest.insert(1, str(url))

def getResult(event):
    dTemp.delete(0, END)
    dName.delete(0, END)
    unit = hidden.get()
    zipc = zipE.get()
    area = countryE.get()
    info = getInfo(str(zipc), str(area), str(unit))
    name = getName(info)
    temp = getTemp(info)
    dName.insert(1, name)
    dTemp.insert(1, temp)
  
    
root = Tk()

root.wm_title("Weather")

Label(root, text="Weather App by Santiago Uriarte").grid(row=0, column=0, columnspan=2, sticky=W)

Label(root, text="Zip Code").grid(row=1, column=0, sticky=W, padx=4)
zipE = Entry(root)
zipE.grid(row=1, column=1, columnspan=2, sticky=E, pady=4)

Label(root, text="Country").grid(row=2, column=0, sticky=W, padx=4)
countryE = Entry(root)
countryE.grid(row=2, column=1, columnspan=2, sticky=E, pady=4)

Label(root, text="Units").grid(row=3, column=0, sticky=W, padx=4)
imp = Button(root, text="Imperial")
imp.grid(row=3, column=1, sticky=E+W, pady=4)
met = Button(root, text="Metric")
met.grid(row=3, column=2, sticky=E+W, pady=4)
imp.bind("<Button-1>", setUnitI)
met.bind("<Button-1>", setUnitM)

Label(root, text="Result").grid(row=4, column=0, sticky=W, padx=4)

Label(root, text="City").grid(row=5, column=0, sticky=W, padx=4)
dName = Entry(root)
dName.grid(row=5, column=1, columnspan=2, sticky=W, pady=4)

Label(root, text="Temperature").grid(row=6, column=0, sticky=W, padx=4)
dTemp = Entry(root)
dTemp.grid(row=6, column=1, columnspan=2, sticky=W, pady=4)

dUnits = StringVar()
Label(root, textvariable=dUnits).grid(row=6, column=3)

hidden = Entry(root)

'''
urlTest = Entry(root)
urlTest.grid(row=8, column=0, columnspan=3, sticky=E+W, pady=4)
'''


submit = Button(root, text="Submit")
submit.bind("<Button-1>", getResult)
submit.grid(row=7, column=1, columnspan=2, sticky=E+W, pady=4)

reset_fields = Button(root, text="Reset")
reset_fields.bind("<Button-1>", reset)
reset_fields.grid(row=7, column=0, sticky=E+W, pady=4)

root.mainloop()