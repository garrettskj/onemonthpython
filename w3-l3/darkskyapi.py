#!/usr/bin/python3

import forecastio
from geopy.geocoders import Nominatim

# Enter an Address for LAT/LONG lookup
address = "15855 SW Stratford Loop, 97224"
#address = "15855 SW Stratford Loop, Portland, Oregon"

def get_weather(address):

	# specify your API key
	ds_apikey = "70066064325e7ce88afbcc4dd07a7595"

	# do the lookup
	location = Nominatim().geocode(address)

	if location != None:
            # create a forecast object
	    forecast = forecastio.load_forecast(ds_apikey, location.latitude, location.longitude, units='us').currently()
	    return (f"It is currently {forecast.temperature} degress near {address}.")
	else:
	    return ("Invalid Address!")

print (get_weather(address))
