#!/usr/bin/python3

import forecastio

def get_weather(geo_lat, geo_long):

	# specify your API key
        # 
        # This key is invalid as of 20190316
        # it exists purely as a reference.
        #
	ds_apikey = "70066064325e7ce88afbcc4dd07a7595"

	# do the lookup
	location = [geo_lat, geo_long]

	if len(location) <=3 or len(location) >= 3:
            # create a forecast object
	    forecast = forecastio.load_forecast(ds_apikey, geo_lat, geo_long, units='us').currently()
	    return (f"It is currently {forecast.temperature} degress.")
	else:
	    return ("Invalid Address!")

print (get_weather('45.585709', '-122.590981'))
